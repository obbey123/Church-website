// Scroll animation
document.addEventListener("DOMContentLoaded", () => {
  const elements = document.querySelectorAll(".fade-in-on-scroll");

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("fade-in");
      }
    });
  }, { threshold: 0.1 });

  elements.forEach(el => observer.observe(el));
});

// Navigation menu toggle
document.addEventListener("DOMContentLoaded", function () {
  const menuToggle = document.getElementById('menu-toggle');
  const navMenu = document.getElementById('nav-menu');

  menuToggle.addEventListener('click', () => {
    navMenu.classList.toggle('show');
  });

  document.addEventListener('click', (e) => {
    if (!navMenu.contains(e.target) && !menuToggle.contains(e.target)) {
      navMenu.classList.remove('show');
    }
  });
});
