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