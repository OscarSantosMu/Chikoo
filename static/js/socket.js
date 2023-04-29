
function agregarMensaje() {
  var texto = document.querySelector("input[type=text]").value;
  if (texto) {
    var mensaje = document.createElement("div");
    var textoMensaje = document.createTextNode(texto);
    mensaje.appendChild(textoMensaje);
    mensaje.classList.add("chat-message", "chat-message-right");
    document.querySelector(".chat-area").appendChild(mensaje);
    document.querySelector("input[type=text]").value = "";
    document.querySelector("input[type=text]").focus();
  }
  procesarMensaje(texto)
}

function procesarMensaje(texto) {
  fetch('/register', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ 'email': 'fmaldonado824@gmail.com', "display_name":"Fernando" })
  })
  .then(res => console.log(res))
  .catch(err => console.error(err))

  fetch('/manage_message', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ 'message': texto })
  })
    .then(response => response.json())
    .then(data => {
      if (data.mensaje) {
        var msg = document.createElement("div");
        var textoMensaje = document.createTextNode(selectClass(data.mensaje));
        msg.appendChild(textoMensaje);
        msg.classList.add("chat-message", "chat-message-left");
        document.querySelector(".chat-area").appendChild(msg);
        document.querySelector("input[type=text]").value = "";
        document.querySelector("input[type=text]").focus();
      }
    })
    .catch(error => {
      console.error('Error:', error);
    });
}

function selectClass(msg) {
  switch (msg) {
    case 'Generate Pre-consult':
      responses = [
        '¡Hola soy Chikoo tu asistente virtual 😉! Estaré super encantado de apoyarte a crear tu primer pre-consulta para la proxima vez que visites un consultorio médico 👨‍⚕️👩‍⚕️',
        'Para empezar necesitare que me indiques si la pre-consulta que necesitas es para tí o si es la pre-consulta de alguien más'
      ]
      return '¡Hola soy Chikoo tu asistente virtual 😉! Estaré super encantado de apoyarte a crear tu primer pre-consulta para la proxima vez que visites un consultorio médico 👨‍⚕️👩‍⚕️'

    case 'Name':
      return '¡Solo las personas cool tienen ese nombre! 🤗 \n\n Ahora necesitare que me apoyes dandome la información acerca de tu edad exacta 📅'

    case 'Age':
      return 'Super, ¿Qué tal si ahora me apoyas con tu lugar de nacimiento? 🌎'

    case 'Place of Birth':
      return 'Excelente, ya casi acabamos ⏰ Necesito que me apoyes con tu numero de identificación nacional, puede ser un personal ID o tu CURP 📎'

    case 'Personal id':
      return '¡Muchas Gracias!, por ultimo solo necesito tu numero de telefono 📞'

    default:
      return 'Testing, atention please'
  }
}

function activarConEnter(inputId, funcion) {
  var input = document.getElementById(inputId);
  input.addEventListener("keyup", function (event) {
    if (event.key === 'Enter') {
      event.preventDefault();
      funcion();
    }
  });
}

activarConEnter("messageHolder", agregarMensaje);

