document.querySelectorAll("form[data-static-only]").forEach((form) => {
    const notice = document.createElement("p");
    notice.className = "pages-backend-notice";
    notice.setAttribute("role", "status");
    notice.setAttribute("aria-live", "polite");
    notice.textContent =
        "Este sitio está publicado como una página estática. Las solicitudes no se envían ni se guardan hasta conectar un backend.";
    form.prepend(notice);

    form.addEventListener("submit", (event) => {
        event.preventDefault();
        notice.textContent =
            "No se envió la solicitud. Para recibir reservas o cancelaciones, este sitio necesita un backend configurado.";
    });
});
