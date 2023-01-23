from fastapi import FastAPI
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Table
from firebase_admin import credentials, storage, initialize_app
import firebase_admin

"""
    TODO
    1.- GET THE URL THEN SEARCH THE HASH_KEY IN THE URL'S TABLE AND GET THE URL
    2.- GET ALL THE DATA FROM THE URL BODY 
    3.- TRANSFORM THE BODY DATA INTO AN OBJECT
    5.- FULLFILL EACH PDF INPUT WITH THE INFORMATION   
    7.- SEND THAT PDF TO THE QR CODE GENERATOR
"""

# Initialize firebase app
cred = credentials.Certificate("./firebase_credentials.json")
firebase_app = firebase_admin.initialize_app(cred, {
    'storageBucket': 'chikoo-ac2ab.appspot.com'
})
print(type(firebase_app))


# Initialize REST API
app = FastAPI()

@app.get("/")
def read_root() -> object:
    return {"Hello": "World"}


@app.get("/pdf")
def generate_pdf() -> object:
    """
        Generates a PDF file, stores it in Firebase Storage and returns the download url to the user
        Returns: Json with the URL of the PDF file stored in Firebase Storage
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
    url = store_pdf_in_firebase(firebase_app)
    return {"pdf": url}


def store_pdf_in_firebase(fb_app: firebase_admin.App) -> str:
    """
        Stores the PDF file in Firebase Storage
        Returns: The Firebase Storage URL
    """

    bucket = storage.bucket(app=fb_app)
    pdf_blob = bucket.blob("hello_world.pdf")
    pdf_blob.upload_from_filename("hello_world.pdf")
    pdf_url = pdf_blob.generate_signed_url(expiration=3000000000)
    return pdf_url
