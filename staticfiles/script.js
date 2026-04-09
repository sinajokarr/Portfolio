document.addEventListener('DOMContentLoaded', () => {
    // Animation for elements appearing on scroll
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = "1";
                entry.target.style.transform = "translateY(0)";
            }
        });
    });

    const hiddenElements = document.querySelectorAll('.row, .skill-box, .contact-form');
    hiddenElements.forEach((el) => {
        el.style.opacity = "0";
        el.style.transform = "translateY(20px)";
        el.style.transition = "all 0.6s ease";
        observer.observe(el);
    });

    // Simple Form Handler UI
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const btn = document.querySelector('.btn-submit');
            const originalText = btn.innerText;
            btn.innerText = "SENDING...";
            
            setTimeout(() => {
                btn.style.background = "#10b981";
                btn.innerText = "SENT SUCCESSFULLY";
                contactForm.reset();
                setTimeout(() => {
                    btn.style.background = "#2563eb";
                    btn.innerText = originalText;
                }, 3000);
            }, 1500);
        });
    }
});