---
publish: true
title: Sobre Mí
created: 2026-07-18T14:50:18.601-03:00
modified: 2026-07-23
---

> [!info] ¡Bienvenido(a)!
> Esta es tu página de inicio. Aquí encontrarás todo lo que necesitas saber sobre mi trayectoria, mis investigaciones y mi trabajo. Lee en el orden sugerido para tener la mejor experiencia posible. 😊

## 📚 ¿Por dónde empezar?

### 1️⃣ Primer paso: Sobre mí

<img src="../assets/profilepic.jpeg" alt="Pedro Henrique" width="160" style="border-radius: 50%; float: right; margin-left: 1.5rem; margin-bottom: 1rem; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">

Soy Pedro Henrique, estudiante de Ingeniería Informática en el [Instituto Federal Fluminense](https://portal1.iff.edu.br/), en Bom Jesus do Itabapoana, en el interior de Río de Janeiro, Brasil. Desde 2022 vengo construyendo un puente entre la **ciencia de la computación** y la **astronomía**, trabajando en proyectos de investigación que exploran poblaciones estelares y la estructura de la Vía Láctea.

Mi pasión está en la intersección entre **métodos computacionales** y **problemas astrofísicos**. Creo que las herramientas de código abierto y los flujos de trabajo reproducibles son esenciales para avanzar la ciencia y hacerla más accesible para todos.

### 🌐 Redes Sociales

Si quieres ponerte en contacto, ¡envíame un correo!

- 💻 [GitHub](https://github.com/pedroiff0)
- 💼 [LinkedIn](https://www.linkedin.com/in/pedroiff0/)
- 📸 [Instagram](https://instagram.com/fckpeeh)
- 🔬 [ORCID](https://orcid.org/0009-0003-6724-4640)
- ✉️ [Correo](mailto:pedroiff0@gmail.com)

### 📬 Contáctame

¿Prefieres no abrir tu cliente de correo? Completa los campos de abajo y el mensaje llega directo a mi bandeja de entrada.

<form id="contact-form" class="contact-form">
  <input type="text" name="from_name" placeholder="Tu nombre" required>
  <input type="email" name="reply_to" placeholder="Tu correo" required>
  <textarea name="message" placeholder="Tu mensaje" rows="5" required></textarea>
  <button type="submit">Enviar</button>
  <p id="contact-form-status"></p>
</form>

<script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js"></script>
<script>
(function() {
  // TODO(Pedro): reemplaza con tus credenciales de https://dashboard.emailjs.com
  // (crea una cuenta gratis, un Email Service y un Email Template con las
  // variables from_name / reply_to / message usadas en el formulario de arriba).
  var EMAILJS_PUBLIC_KEY = "fh5Z3HcsBAXFKJ-Jd";
  var EMAILJS_SERVICE_ID = "service_myxxjn7";
  var EMAILJS_TEMPLATE_ID = "template_1baqk12";

  var form = document.getElementById("contact-form");
  var status = document.getElementById("contact-form-status");
  if (!form || window.emailjs === undefined) return;
  emailjs.init({ publicKey: EMAILJS_PUBLIC_KEY });

  form.addEventListener("submit", function(e) {
    e.preventDefault();
    if (EMAILJS_PUBLIC_KEY.indexOf("AQUI") !== -1) {
      status.textContent = "El formulario aún no está configurado — por ahora, envía un correo directamente.";
      return;
    }
    status.textContent = "Enviando…";
    emailjs.sendForm(EMAILJS_SERVICE_ID, EMAILJS_TEMPLATE_ID, form).then(
      function() {
        status.textContent = "Mensaje enviado — ¡gracias por escribir!";
        form.reset();
      },
      function(err) {
        status.textContent = "No se pudo enviar en este momento. Intenta de nuevo o escribe un correo directamente.";
      }
    );
  });
})();
</script>

### 2️⃣ Segundo paso: Áreas de interés

- **Astrofísica**: Arqueología galáctica, poblaciones estelares, estructura y evolución química de la Vía Láctea, análisis de grandes volúmenes de datos astronómicos.
- **Ciencia de la Computación**: Computación científica, pipelines de datos, aprendizaje automático en astronomía, desarrollo de código abierto.
- **Psicoanálisis**:

### 3️⃣ Tercer paso: Explorar el contenido

> [!warning] Versión en español todavía en preparación
> El resto del contenido de este sitio aún no está traducido al español — está disponible en [portugués](/pt-br/) (idioma original) y, parcialmente, en [inglés](/en/).

Para navegar mi trabajo, explora las secciones del sitio (en portugués/inglés):

<div class="media-carousel">
  <a href="/pt-br/research" class="carousel-slide">
    <img src="/assets/illustrations/research.svg" alt="Investigación" />
    <div class="slide-caption">Investigación</div>
  </a>
  <a href="/pt-br/resource" class="carousel-slide">
    <img src="/assets/illustrations/resource.svg" alt="Recursos" />
    <div class="slide-caption">Recursos</div>
  </a>
  <a href="/pt-br/resource/engenharia-de-computação" class="carousel-slide">
    <img src="/assets/illustrations/classes.svg" alt="Asignaturas" />
    <div class="slide-caption">Asignaturas</div>
  </a>
  <a href="/pt-br/media" class="carousel-slide">
    <img src="/assets/febic2024/febic.jpeg" alt="Medios" />
    <div class="slide-caption">Medios</div>
  </a>
  <a href="/pt-br/projects" class="carousel-slide">
    <img src="/assets/illustrations/projects.svg" alt="Proyectos" />
    <div class="slide-caption">Proyectos</div>
  </a>
  <a href="/pt-br/blog" class="carousel-slide">
    <img src="/assets/illustrations/toolkit.svg" alt="Blog" />
    <div class="slide-caption">Blog</div>
  </a>
</div>

- [Investigación](pt-br/research/) — Conoce mis proyectos actuales y publicaciones.
- [Recursos](pt-br/resource/) — Materiales, scripts y herramientas útiles que he desarrollado o utilizo.
- [Asignaturas](pt-br/resource/engenharia-de-computação/) — Mis apuntes y trabajos de la universidad.
- [Medios](pt-br/media/) — Participaciones en eventos, ferias y presentaciones.
- [Proyectos](pt-br/projects/) — Herramientas y aplicaciones que desarrollo fuera de la investigación académica.
- [Blog](pt-br/blog/) — Pensamientos sueltos, tutoriales y reflexiones sobre el camino de la investigación.

Este sitio se escribe primero en **portugués (Brasil)** y se traduce al inglés a medida que el tiempo lo permite — el español es el idioma más reciente en incorporarse, así que todavía queda mucho por traducir. Si notaste algo que falta o está desactualizado, puedes abrir un [issue en el repositorio](https://github.com/pedroiff0/page/issues), o [hacer clic aquí para abrir uno ya completado desde la plantilla de traducción](https://github.com/pedroiff0/page/issues/new?template=traducao.yml).
