from flask import Flask, render_template, request, jsonify
import cohere
from classifications import examples
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from mako.template import Template
from flask_cors import CORS, cross_origin

app = Flask(__name__)

co = cohere.Client('VI8IBNMDAZhU8FoqXh81eoM988zV4f8cjgw0EyBZ')
CORS(app)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/manage_message', methods=['POST'])
def manage_message():
    data = request.get_json()
    mensaje = data.get('message')

    if mensaje:
        co = cohere.Client("VI8IBNMDAZhU8FoqXh81eoM988zV4f8cjgw0EyBZ")
        classifications = co.classify(
            model='large',
            inputs=[mensaje],
            examples=examples)
        prediction = classifications[0].prediction
        return jsonify({'mensaje': prediction})    

@app.route('/register', methods=['POST'])
@cross_origin(origins="https://tigrehacks.me")
def register():
    data = request.get_json()

    email = data['email']
    display_name = data.get('display_name', 'Usuario')
    image_url = "https://www.tigrehacks.me/logo.png"

    email_template = Template(filename='email_template.mako')

    # Renderiza la plantilla con los datos del usuario
    html_content = email_template.render(display_name=display_name, image_url=image_url)

    # Configura el contenido del correo electrónico de bienvenida
    message = MIMEMultipart()
    message['Subject'] = 'Gracias por registrarte en Tigre Hacks 🐯'
    message['From'] = 'bisontech0@gmail.com'
    message['To'] = email
    message.attach(MIMEText(html_content, 'html'))


    # Configura las credenciales de tu servicio de correo electrónico aquí
    username = 'bisontech0@gmail.com'
    password = 'imkkiakbdsletupm'

    # Envía el correo electrónico
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(username, password)
        server.sendmail(username, email, message.as_string())
        server.quit()
        return jsonify({'message': 'Correo electrónico enviado correctamente'}), 200
    except Exception as e:
        print(f'Error al enviar el correo electrónico: {e}')
        return jsonify({'message': 'Error al enviar el correo electrónico'}), 500
