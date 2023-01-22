from fastapi import FastAPI
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table
from reportlab.lib.styles import ParagraphStyle
from firebase_admin import credentials, storage
import firebase_admin

"""
    TODO
    1.- GET THE URL THEN SEARCH THE HASH_KEY IN THE URL'S TABLE AND GET THE URL
    2.- GET ALL THE DATA FROM THE URL BODY 
    3.- TRANSFORM THE BODY DATA INTO AN OBJECT
    4.- INITIALIZE THE PDF CREATOR
    5.- FULLFILL EACH PDF INPUT WITH THE INFORMATION
    6.- SAVE THE PDF 
    7.- SEND THAT PDF TO THE QR CODE GENERATOR
"""

# Initialize firebase app
cred = credentials.Certificate("./firebase_admin.json")
firebase_app= firebase_admin.initialize_app(cred, {
    'storageBucket': 'chikoo-ac2ab.appspot.com'
})

# url="https://chikoo.github-pages.com/2ASK3KS"
# HASH_KEY = url.split("/")[3]

# Initialize REST API
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/pdf")
def generate_pdf():
    """
        Generates a PDF file, stores it in Firebase Storage and returns the download url to the user 
    """

    pdf_file = SimpleDocTemplate("hello_world.pdf", pagesize=letter)
    elements = []
    
    # Add H1 header
    elements.append(Paragraph("<h1>Hello World!</h1>"))

    # Add image
    elements.append(Image("dogo.png"))

    # Add table
    data = [['name', 'age', 'city of residence', 'diabetic status'],
            ['John Doe', '32', 'New York', 'No']]
    table = Table(data)
    elements.append(table)
    pdf_file.build(elements)

    # Store the PDF in Firebase Storage
    bucket = storage.bucket(app=firebase_app)
    pdf_blob = bucket.blob("hello_world.pdf")
    pdf_blob.upload_from_filename("hello_world.pdf")
    pdf_url = pdf_blob.generate_signed_url(expiration=3000000000)
    return {"pdf": pdf_url}
