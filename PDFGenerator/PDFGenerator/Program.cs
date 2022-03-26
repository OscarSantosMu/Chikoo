
// Must have write permissions to the path folder
string path = "D:\\dotnet\\PDFGenerator\\demo.pdf";
PdfWriter writer = new PdfWriter(path);
PdfDocument pdf = new PdfDocument(writer);
Document document = new Document(pdf);

// Add Header
Paragraph header = new Paragraph("Medical Preconsultation")
   .SetTextAlignment(TextAlignment.CENTER)
   .SetFontSize(20);

// New line
Paragraph newline = new Paragraph(new Text("\n"));

document.Add(newline);
document.Add(header);

// Add subheader
Paragraph subheader = new Paragraph("Patient situation")
   .SetTextAlignment(TextAlignment.CENTER)
   .SetFontSize(15);
document.Add(subheader);

// Line separator
LineSeparator ls = new LineSeparator(new SolidLine());
document.Add(ls);

// Add paragraph1
Paragraph paragraph1 = new Paragraph("Lorem ipsum " +
   "dolor sit amet, consectetur adipiscing elit, " +
   "sed do eiusmod tempor incididunt ut labore " +
   "et dolore magna aliqua.");
document.Add(paragraph1);

// Add image
Image img = new Image(ImageDataFactory
   .Create(@$"{path}\..\img\medical.jpg"))
   .SetTextAlignment(TextAlignment.CENTER);
document.Add(img);

// Table
Table table = new Table(2, false);
Cell cell11 = new Cell(1, 1)
   .SetBackgroundColor(ColorConstants.GRAY)
   .SetTextAlignment(TextAlignment.CENTER)
   .Add(new Paragraph("Symptoms"));
Cell cell12 = new Cell(1, 1)
   .SetBackgroundColor(ColorConstants.GRAY)
   .SetTextAlignment(TextAlignment.CENTER)
   .Add(new Paragraph("Yes/No"));

Cell cell21 = new Cell(1, 1)
   .SetTextAlignment(TextAlignment.CENTER)
   .Add(new Paragraph("Pain"));
Cell cell22 = new Cell(1, 1)
   .SetTextAlignment(TextAlignment.CENTER)
   .Add(new Paragraph("Yes"));

Cell cell31 = new Cell(1, 1)
   .SetTextAlignment(TextAlignment.CENTER)
   .Add(new Paragraph("Headaches"));
Cell cell32 = new Cell(1, 1)
   .SetTextAlignment(TextAlignment.CENTER)
   .Add(new Paragraph("No"));

Cell cell41 = new Cell(1, 1)
   .SetTextAlignment(TextAlignment.CENTER)
   .Add(new Paragraph("Runny nose"));
Cell cell42 = new Cell(1, 1)
   .SetTextAlignment(TextAlignment.CENTER)
   .Add(new Paragraph("No"));

table.AddCell(cell11);
table.AddCell(cell12);
table.AddCell(cell21);
table.AddCell(cell22);
table.AddCell(cell31);
table.AddCell(cell32);
table.AddCell(cell41);
table.AddCell(cell42);
document.Add(newline);
document.Add(table);

//// Hyper link
//Link link = new Link("click here",
//   PdfAction.CreateURI("https://www.google.com"));
//Paragraph hyperLink = new Paragraph("Please ")
//   .Add(link.SetBold().SetUnderline()
//   .SetItalic().SetFontColor(ColorConstants.BLUE))
//   .Add(" to go www.google.com.");

//document.Add(newline);
//document.Add(hyperLink);

// Page numbers
int n = pdf.GetNumberOfPages();
for (int i = 1; i <= n; i++)
{
    document.ShowTextAligned(new Paragraph(String
       .Format("page" + i + " of " + n)),
        559, 806, i, TextAlignment.RIGHT,
        VerticalAlignment.TOP, 0);
}

// Close document
document.Close();