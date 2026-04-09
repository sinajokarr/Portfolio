document.addEventListener('DOMContentLoaded', () => {
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

    const contactForm = document.getElementById('contactForm');
    
    if (contactForm) {
        contactForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const btn = document.querySelector('.btn-submit');
            const originalText = btn.innerText;
            const originalBg = window.getComputedStyle(btn).backgroundColor;
            
            const nameField = document.getElementById('name');
            const emailField = document.getElementById('email');
            const messageField = document.getElementById('message');

            if (!nameField || !emailField || !messageField) {
                console.error("DOM Error: Missing input IDs.");
                return;
            }

            btn.innerText = "SENDING...";
            btn.disabled = true;
            btn.style.cursor = "not-allowed";
            
            try {
                const response = await fetch('/blog/contact/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ 
                        name: nameField.value, 
                        email: emailField.value, 
                        message: messageField.value 
                    })
                });

                if (response.ok) {
                    btn.style.background = "#10b981";
                    btn.innerText = "SENT SUCCESSFULLY";
                    contactForm.reset();
                } else {
                    throw new Error(`Server Response: ${response.status}`);
                }
                
            } catch (error) {
                console.error('Submission Error:', error);
                btn.style.background = "#ef4444";
                btn.innerText = "FAILED TO SEND";
            } finally {
                setTimeout(() => {
                    btn.style.background = originalBg;
                    btn.innerText = originalText;
                    btn.disabled = false;
                    btn.style.cursor = "pointer";
                }, 3000);
            }
        });
    }
});