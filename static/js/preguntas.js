//1
const menu = document.getElementById('menu');
const sidebar = document.getElementById('sidebar');

menu.addEventListener('click', () => {
    sidebar.classList.toggle('menu-toggle');
    menu.classList.toggle('menu-toggle');
});


//2
document.querySelectorAll('.faq-question').forEach(button => {
    button.addEventListener('click', () => {
        const faqItem = button.parentElement;
        
        // Cerrar otros elementos abiertos (opcional, para un efecto más limpio)
        document.querySelectorAll('.faq-item').forEach(item => {
            if (item !== faqItem) {
                item.classList.remove('active');
            }
        });

        // Alternar el estado actual
        faqItem.classList.toggle('active');
    });
});