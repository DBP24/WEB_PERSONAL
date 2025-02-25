
document.addEventListener("DOMContentLoaded", function() {
  // Referencias a elementos del DOM
  const header = document.getElementById('site-header');
  const menuButton = document.getElementById('mobile-menu-button');
  const mobileMenuContainer = document.getElementById('mobile-menu-container');
  const mobileLinks = document.querySelectorAll('.mobile-link');
  
  // Variables para controlar el scroll
  let lastScrollTop = 0;
  const scrollThreshold = 100;
  
  // Función para controlar el estado del header al hacer scroll
  function handleScroll() {
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    
    // Añadir clase de fondo cuando se hace scroll
    if (scrollTop > 20) {
      header.classList.add('header-scrolled');
    } else {
      header.classList.remove('header-scrolled');
    }
    
    // Ocultar/mostrar header según dirección del scroll
    if (scrollTop > lastScrollTop && scrollTop > scrollThreshold) {
      // Scrolling hacia abajo
      header.classList.add('header-hidden');
    } else {
      // Scrolling hacia arriba
      header.classList.remove('header-hidden');
    }
    
    lastScrollTop = scrollTop <= 0 ? 0 : scrollTop; // Ajuste para Safari
  }
  
  // Event listener para el scroll
  window.addEventListener('scroll', handleScroll, { passive: true });
  
  // Función para abrir/cerrar el menú móvil
  function toggleMobileMenu() {
    menuButton.classList.toggle('active');
    mobileMenuContainer.classList.toggle('active');
    
    // Prevenir scroll del body cuando el menú está abierto
    document.body.style.overflow = menuButton.classList.contains('active') ? 'hidden' : '';
  }
  
  // Event listener para el botón de menú
  menuButton.addEventListener('click', toggleMobileMenu);
  
  // Cerrar menú al hacer clic en un enlace
  mobileLinks.forEach(link => {
    link.addEventListener('click', function() {
      menuButton.classList.remove('active');
      mobileMenuContainer.classList.remove('active');
      document.body.style.overflow = '';
    });
  });
  
  // Cerrar menú al redimensionar la ventana
  window.addEventListener('resize', function() {
    if (window.innerWidth > 768 && menuButton.classList.contains('active')) {
      menuButton.classList.remove('active');
      mobileMenuContainer.classList.remove('active');
      document.body.style.overflow = '';
    }
  });
  
  // Resaltar página actual en la navegación
  const currentPath = window.location.pathname;
  const allNavLinks = document.querySelectorAll(".nav-link, .mobile-link");
  
  allNavLinks.forEach(link => {
    if (link.getAttribute("href") === currentPath) {
      link.classList.add("text-white");
      link.classList.add("font-medium");
    }
  });
  
  // Inicializar el estado del header
  handleScroll();
});
