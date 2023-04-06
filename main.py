import os
import json
from dotenv import load_dotenv

from fastapi import FastAPI, Request
import uvicorn

from firebase_admin import credentials, storage, initialize_app
import firebase_admin

from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

from chikoo_document import ChikooDocument
from testing_info import family_history, foods_per_week, data, activities_per_week

load_dotenv()
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
client = Client(account_sid, auth_token)

# Initialize firebase app

with open('./firebase_credentials.json', 'r', encoding="utf-8") as f:
    firebase_creds = credentials.Certificate(json.load(f))

firebase_app = initialize_app(firebase_creds, {
    'storageBucket': os.environ.get('STORAGE_BUCKET')
})


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
    chikoo = ChikooDocument(data=data, foods_per_week=foods_per_week, family_history=family_history, activities=activities_per_week)
    document = chikoo.create_document()
    url = store_pdf_in_firebase(firebase_app)
    return {"pdf": url}


@app.post("/bot")
async def bot(request: Request):
    mensaje = (await request.form())["Body"]
    remitente = (await request.form())["From"]

    if "cat" in mensaje.lower():
        respuesta = "miau miau miau"
    elif "dog" in mensaje.lower():
        respuesta = "woof woof woof"
    else:
        respuesta = "I love animals!"

    # Crear una respuesta de TwiML
    twiml_respuesta = MessagingResponse()
    twiml_respuesta.message(from_="whatsapp:+14155238886",
                            to="whatsapp:+5219213043932", body=respuesta)
    send_msg(respuesta)
    return str(twiml_respuesta)


def send_msg(msg):
    client.messages.create(
        from_="whatsapp:+14155238886",
        to="whatsapp:+5219213043932", body=msg)


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


if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
