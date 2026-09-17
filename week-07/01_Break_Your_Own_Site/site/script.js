const menuButton = document.querySelector('.menu-toggle');
const mobileMenu = document.querySelector('#mobile-menu');

if (menuButton && mobileMenu) {
  const closeMenu = () => {
    menuButton.setAttribute('aria-expanded', 'false');
    menuButton.setAttribute('aria-label', 'Open navigation menu');
    mobileMenu.hidden = true;
    document.body.classList.remove('menu-open');
  };

  menuButton.addEventListener('click', () => {
    const isOpen = menuButton.getAttribute('aria-expanded') === 'true';
    menuButton.setAttribute('aria-expanded', String(!isOpen));
    menuButton.setAttribute('aria-label', isOpen ? 'Open navigation menu' : 'Close navigation menu');
    mobileMenu.hidden = isOpen;
    document.body.classList.toggle('menu-open', !isOpen);
  });

  mobileMenu.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
  window.addEventListener('resize', () => { if (window.innerWidth > 800) closeMenu(); });
}


const contactForm = document.querySelector('#contact-form');
if (contactForm) {
  const submitButton = document.querySelector('#submit-button');
  const status = document.querySelector('#form-status');
  const fields = {
    name: { input: document.querySelector('#name'), error: document.querySelector('#name-error') },
    email: { input: document.querySelector('#email'), error: document.querySelector('#email-error') },
    message: { input: document.querySelector('#message'), error: document.querySelector('#message-error') }
  };
  const clearErrors = () => Object.values(fields).forEach(({error}) => { error.textContent = ''; });
  const validate = () => {
    clearErrors(); let ok = true;
    const name = fields.name.input.value.trim();
    const email = fields.email.input.value.trim();
    const message = fields.message.input.value.trim();
    if (name.length < 2) { fields.name.error.textContent = 'Please enter at least 2 characters.'; ok = false; }
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) { fields.email.error.textContent = 'Please enter a valid email address.'; ok = false; }
    if (message.length < 10) { fields.message.error.textContent = 'Please enter at least 10 characters.'; ok = false; }
    if (message.length > 1000) { fields.message.error.textContent = 'Message is too long.'; ok = false; }
    return ok;
  };
  contactForm.addEventListener('submit', (event) => {
    event.preventDefault(); status.textContent = '';
    if (contactForm.website && contactForm.website.value) { status.textContent = 'Submission blocked by spam protection.'; return; }
    if (!validate()) { status.textContent = 'Please correct the highlighted fields before submitting.'; return; }
    submitButton.disabled = true;
    status.textContent = 'Message validated locally. No message was sent; use LinkedIn for the actual conversation.';
    window.setTimeout(() => { submitButton.disabled = false; }, 1200);
  });
}
