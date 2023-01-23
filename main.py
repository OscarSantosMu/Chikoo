from fastapi import FastAPI
from pdf_filler import fill_pdf
from firebase_admin import credentials, storage, initialize_app
import firebase_admin

# Initialize firebase app
cred = credentials.Certificate("./firebase_credentials.json")
firebase_app = firebase_admin.initialize_app(cred, {
    'storageBucket': 'chikoo-ac2ab.appspot.com'
})

data = {
    'direct_fillment': False,
    'name_of_filler_person': 'David Lazaro',
    'name': 'David',
    'age': '22',
    'sex': 'Masculine',
    'last_name': 'Lazaro Fernandez',
    'birth_date': '13/12/2000',
    'place_of_birth': 'Minatitlan, Veracruz',
    'adress': 'Sabinas',
    'pc': '1222222',
    'phone_number': 'I prefer not to respond',
    'work_status': 'I prefer not to respond',
}

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
    fill_pdf(data)
    url = store_pdf_in_firebase(firebase_app)
    return {"pdf": url}


def store_pdf_in_firebase(fb_app: firebase_admin.App) -> str:
    """
        Stores the PDF file in Firebase Storage
        Returns: The Firebase Storage URL
    """

    bucket = storage.bucket(app=fb_app)
    pdf_blob = bucket.blob("chikoo.png")
    pdf_blob.upload_from_filename("chikoo.png")
    pdf_url = pdf_blob.generate_signed_url(expiration=3000000000)
    return pdf_url
