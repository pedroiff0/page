---
publish: true
title: About Me
created: 2026-07-18T14:25:13.277-03:00
---

> [!info] Welcome!
> This is your starting page! Here you will find everything you need to know about my journey, research, and work. Read in the suggested order to have the best possible experience. 😊

## 📚 Where to start?

### 1️⃣ First step: About me

<img src="../assets/profilepic.jpeg" alt="Pedro Henrique" width="160" style="border-radius: 50%; float: right; margin-left: 1.5rem; margin-bottom: 1rem; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">

I am Pedro Henrique, an undergraduate Computer Engineering student at the [Fluminense Federal Institute](https://portal1.iff.edu.br/), in Rio de Janeiro, Brazil. Since 2022, I have been building a bridge between **computer science** and **astronomy**, working on research projects that explore stellar populations and the structure of the Milky Way.

My passion lies at the intersection of **computational methods** and **astrophysical problems**. I believe that open-source tools and reproducible workflows are essential to advancing science and making it more accessible to everyone.

### 🌐 Social Media

If you'd like to get in touch, send an email!

- 💻 [GitHub](https://github.com/pedroiff0)
- 💼 [LinkedIn](https://www.linkedin.com/in/pedroiff0/)
- 📸 [Instagram](https://instagram.com/fckpeeh)
- 🔬 [ORCID](https://orcid.org/0009-0003-6724-4640)
- ✉️ [Email](mailto:pedroiff0@gmail.com)

### 📬 Get in touch

Prefer not to open your email client? Fill in the fields below and the message lands straight in my inbox.

<form id="contact-form" class="contact-form">
  <input type="text" name="from_name" placeholder="Your name" required>
  <input type="email" name="reply_to" placeholder="Your email" required>
  <textarea name="message" placeholder="Your message" rows="5" required></textarea>
  <button type="submit">Send</button>
  <p id="contact-form-status"></p>
</form>

<script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js"></script>
<script>
(function() {
  // TODO(Pedro): replace with your credentials from https://dashboard.emailjs.com
  // (create a free account, an Email Service and an Email Template using the
  // from_name / reply_to / message variables from the form above).
  var EMAILJS_PUBLIC_KEY = "fh5Z3HcsBAXFKJ-Jd";
  var EMAILJS_SERVICE_ID = "service_myxxjn7";
  var EMAILJS_TEMPLATE_ID = "template_1baqk12";

  var form = document.getElementById("contact-form");
  var status = document.getElementById("contact-form-status");
  if (!form || window.emailjs === undefined) return;
  emailjs.init({ publicKey: EMAILJS_PUBLIC_KEY });

  form.addEventListener("submit", function(e) {
    e.preventDefault();
    if (EMAILJS_PUBLIC_KEY.indexOf("HERE") !== -1) {
      status.textContent = "Form not configured yet — please email me directly for now.";
      return;
    }
    status.textContent = "Sending…";
    emailjs.sendForm(EMAILJS_SERVICE_ID, EMAILJS_TEMPLATE_ID, form).then(
      function() {
        status.textContent = "Message sent — thanks for reaching out!";
        form.reset();
      },
      function(err) {
        status.textContent = "Couldn't send it right now. Try again or email me directly.";
      }
    );
  });
})();
</script>

### 2️⃣ Second step: Areas of Interest

- **Astrophysics**: Galactic archaeology, stellar populations, Milky Way structure and chemical evolution, large-scale astronomical data analysis.
- **Computer Science**: Scientific computing, data pipelines, machine learning applications in astronomy, open-source development.
- **Psychoanalysis**:

### 3️⃣ Third step: Explore the content

To navigate my work, explore the sections of this site:

<div class="media-carousel">
  <a href="/en/research" class="carousel-slide">
    <img src="/assets/illustrations/research.svg" alt="Research" />
    <div class="slide-caption">Research</div>
  </a>
  <a href="/en/resource" class="carousel-slide">
    <img src="/assets/illustrations/resource.svg" alt="Resources" />
    <div class="slide-caption">Resources</div>
  </a>
  <a href="/en/resource/engenharia-de-computação" class="carousel-slide">
    <img src="/assets/illustrations/classes.svg" alt="Classes" />
    <div class="slide-caption">Classes</div>
  </a>
  <a href="/en/media" class="carousel-slide">
    <img src="/assets/febic2024/febic.jpeg" alt="Media" />
    <div class="slide-caption">Media</div>
  </a>
  <a href="/en/projects" class="carousel-slide">
    <img src="/assets/illustrations/projects.svg" alt="Projects" />
    <div class="slide-caption">Projects</div>
  </a>
  <a href="/en/blog" class="carousel-slide">
    <img src="/assets/illustrations/toolkit.svg" alt="Blog" />
    <div class="slide-caption">Blog</div>
  </a>
</div>

- [Research](en/research/) — Learn about my current projects and publications.
- [Resources](en/resource/) — Materials, scripts, and useful tools I've developed or use.
- [Classes](en/resource/engenharia-de-computação/) — My notes and coursework from college.
- [Media](en/media/) — Participations in events, fairs, and presentations.
- [Projects](en/projects/) — Tools and applications I build outside of academic research.
- [Blog](en/blog/) — Random thoughts, tutorials, and reflections on the research journey.

This site is written in two languages: all content is first written in **Portuguese (Brazil)** and translated to English as time allows — so not every page has an English version yet. If you noticed something missing or outdated in translation, feel free to open an [issue in the repository](https://github.com/pedroiff0/page/issues), or [click here to open one pre-filled from the translation template](https://github.com/pedroiff0/page/issues/new?template=traducao.yml).
