from fastapi import FastAPI, Request
from firebase_admin import credentials, storage, initialize_app
import firebase_admin
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import uvicorn

from pdf_filler import fill_pdf


account_sid = 'AC01a324f7bb0dcceb216c28547f79bc01'
auth_token = 'f852f9489364de450637f2b3290faf19'
client = Client(account_sid, auth_token)

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


@app.post("/response")
async def response(request: Request):
    # Obtener el message entrante y el número de teléfono del sender
    message = (await request.form())["Body"]
    sender = (await request.form())["From"]

    # Procesar el message entrante y enviar una respuesta
    # Puedes personalizar esta lógica según tus necesidades
    respuesta = f'Hola! Has enviado el siguiente message: {message}. Tu número de teléfono es: {sender}'

    # Crear una respuesta de TwiML
    twiml_response = MessagingResponse()
    twiml_response.message(response)

    return str(twiml_response)


@app.post("/bot")
async def bot(request: Request):
    # Obtener el mensaje entrante y el número de teléfono del remitente
    mensaje = (await request.form())["Body"]
    remitente = (await request.form())["From"]

    # Procesar el mensaje entrante y enviar una respuesta
    # Verificar si el mensaje contiene las palabras "cat" o "dog"
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
