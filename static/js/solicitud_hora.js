const menu = document.getElementById('menu');
const sidebar = document.getElementById('sidebar');

menu.addEventListener('click', () => {
    sidebar.classList.toggle('menu-toggle');
    menu.classList.toggle('menu-toggle');
});

//Ventana modal
const abrir_modal = document.getElementById("open-modal");
const modal = document.getElementById("modal");
const cerrar = document.getElementById("close-modal");

abrir_modal.addEventListener("click", (e) => {
    e.preventDefault();
    modal.showModal();
    abrir_modal.classList.add("active");
});

cerrar.addEventListener("click", (e) => {
    e.preventDefault();
    modal.close();
});

modal.addEventListener("close", () => {
    abrir_modal.classList.remove("active");
    abrir_modal.blur();
});

//key 
// Inicializar EmailJS
emailjs.init({
    publicKey: "PJr2sRksukIdtcFyB"
});

// Obtener formulario
const formulario = document.getElementById("formulario-solicitud");

// Evento enviar
formulario.addEventListener("submit", (e) => {


    const parametros = {
        nombre: document.getElementById("nombre").value,
        curso: document.getElementById("curso").value,
        correo: document.getElementById("correo").value,
        fecha: document.getElementById("fecha").value,
        motivo: document.getElementById("motivo").value
    };

    console.log("Datos enviados:", parametros);

    emailjs.send(
        "service_b4x81gn",
        "template_tjdc5sw",
        parametros
    )
    .then((response) => {
        console.log("Éxito:", response);

        alert("Solicitud enviada correctamente.");
        formulario.reset();
    })
    .catch((error) => {
        console.error("Error completo:", error);

        if (error.status) {
            console.log("Status:", error.status);
        }

        if (error.text) {
            console.log("Texto:", error.text);
        }

        alert("Error al enviar la solicitud. Revisa la consola (F12).");
    });
});

const boton = formulario.querySelector("button");

boton.disabled = true;
boton.textContent = "Enviando...";

boton.disabled = false;
boton.textContent = "Enviar Solicitud";
/*========================================
            LOADER
========================================*/

window.addEventListener("load", () => {

    const loader = document.getElementById("pageLoader");

    if (loader) {

        setTimeout(() => {

            loader.classList.add("hidden");

        }, 800);

    }

});