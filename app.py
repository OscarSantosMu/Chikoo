from flask import Flask, render_template, request, jsonify
import cohere
from classifications import examples

app = Flask(__name__)

co = cohere.Client('VI8IBNMDAZhU8FoqXh81eoM988zV4f8cjgw0EyBZ')


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
def register():
    data = request.get_json()

    email = data['email']
    display_name = data.get('display_name', 'Usuario')

    # Configura el contenido del correo electrónico de bienvenida
    message = MIMEText(f'¡Hola {display_name}! Gracias por registrarte en nuestra app. Esperamos que disfrutes de nuestra plataforma.')
    message['Subject'] = 'Gracias por registrarte en la app'
    message['From'] = 'bisontech0@gmail.com'
    message['To'] = email

    # Configura las credenciales de tu servicio de correo electrónico aquí
    username = 'tuemail@gmail.com'
    password = 'tupassword'

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
