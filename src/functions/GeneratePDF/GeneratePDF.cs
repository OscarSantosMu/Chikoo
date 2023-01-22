using System;
using System.IO;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Extensions.Http;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.Logging;
using Newtonsoft.Json;
using iText.IO.Image;
using iText.Kernel.Colors;
using iText.Kernel.Pdf.Action;
using iText.Kernel.Pdf;
using iText.Layout;
using iText.Layout.Element;
using iText.Layout.Properties;
using iText.Kernel.Pdf.Canvas.Draw;

namespace Chikoo.Functions
{
    public static class GeneratePDF
    {
        [FunctionName("GeneratePDF")]
        public static async Task<IActionResult> Run(
            [HttpTrigger(AuthorizationLevel.Anonymous, "get", "post", Route = null)] HttpRequest req,
            ILogger log)
        {
            log.LogInformation("C# HTTP trigger function processed a request.");

            // Create a new PDF document
            using (var stream = new MemoryStream())
            {
                using (var pdf = new PdfDocument(new PdfWriter(stream)))
                {
                    var doc = new Document(pdf);

                    // Add content to the PDF document
                    doc.Add(new Paragraph("Hello, PDF!"));

                    doc.Close();
                }

                // Set the response content type to "application/pdf"
                var response = new FileContentResult(stream.ToArray(), "application/pdf")
                {
                    FileDownloadName = "hello.pdf"
                };

                return response;
            }
        }
    }
}
