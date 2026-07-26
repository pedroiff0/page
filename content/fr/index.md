---
publish: true
title: À propos de moi
created: 2026-07-18T14:50:18.601-03:00
modified: 2026-07-23
published: 2026-07-26T10:01:58.952-03:00
---

> [!info] Bienvenue !
> Voici votre page de départ. Vous y trouverez tout ce qu'il faut savoir sur mon parcours, mes recherches et mon travail. Lisez dans l'ordre suggéré pour la meilleure expérience possible. 😊

## 📚 Par où commencer ?

### 1️⃣ Première étape : à propos de moi

<img src="../assets/profilepic.jpeg" alt="Pedro Henrique" width="160" style="border-radius: 50%; float: right; margin-left: 1.5rem; margin-bottom: 1rem; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">

Je m'appelle Pedro Henrique, étudiant en génie informatique à l'[Institut Fédéral Fluminense](https://portal1.iff.edu.br/), à Bom Jesus do Itabapoana, dans l'intérieur de l'État de Rio de Janeiro, au Brésil. Depuis 2022, je construis un pont entre l'**informatique** et l'**astronomie**, en travaillant sur des projets de recherche qui explorent les populations stellaires et la structure de la Voie lactée.

Ma passion se situe à l'intersection des **méthodes computationnelles** et des **problèmes astrophysiques**. Je crois que les outils open-source et les flux de travail reproductibles sont essentiels pour faire avancer la science et la rendre plus accessible à tous.

### 🌐 Réseaux sociaux

Si vous souhaitez me contacter, envoyez-moi un e-mail !

- 💻 [GitHub](https://github.com/pedroiff0)
- 💼 [LinkedIn](https://www.linkedin.com/in/pedroiff0/)
- 📸 [Instagram](https://instagram.com/fckpeeh)
- 🔬 [ORCID](https://orcid.org/0009-0003-6724-4640)
- ✉️ [E-mail](mailto:pedroiff0@gmail.com)

### 📬 Contactez-moi

Vous préférez ne pas ouvrir votre client e-mail ? Remplissez les champs ci-dessous et le message arrive directement dans ma boîte de réception.

<form id="contact-form" class="contact-form">
  <input type="text" name="from_name" placeholder="Votre nom" required>
  <input type="email" name="reply_to" placeholder="Votre e-mail" required>
  <textarea name="message" placeholder="Votre message" rows="5" required></textarea>
  <button type="submit">Envoyer</button>
  <p id="contact-form-status"></p>
</form>

<script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js"></script>

<script>
(function() {
  // TODO(Pedro): remplacez par vos identifiants depuis https://dashboard.emailjs.com
  // (créez un compte gratuit, un Email Service et un Email Template utilisant les
  // variables from_name / reply_to / message du formulaire ci-dessus).
  var EMAILJS_PUBLIC_KEY = "fh5Z3HcsBAXFKJ-Jd";
  var EMAILJS_SERVICE_ID = "service_myxxjn7";
  var EMAILJS_TEMPLATE_ID = "template_1baqk12";

  var form = document.getElementById("contact-form");
  var status = document.getElementById("contact-form-status");
  if (!form || window.emailjs === undefined) return;
  emailjs.init({ publicKey: EMAILJS_PUBLIC_KEY });

  form.addEventListener("submit", function(e) {
    e.preventDefault();
    if (EMAILJS_PUBLIC_KEY.indexOf("ICI") !== -1) {
      status.textContent = "Le formulaire n'est pas encore configuré — envoyez un e-mail directement pour l'instant.";
      return;
    }
    status.textContent = "Envoi…";
    emailjs.sendForm(EMAILJS_SERVICE_ID, EMAILJS_TEMPLATE_ID, form).then(
      function() {
        status.textContent = "Message envoyé — merci de m'avoir écrit !";
        form.reset();
      },
      function(err) {
        status.textContent = "Impossible d'envoyer pour le moment. Réessayez ou envoyez un e-mail directement.";
      }
    );
  });
})();
</script>

### 2️⃣ Deuxième étape : domaines d'intérêt

- **Astrophysique** : archéologie galactique, populations stellaires, structure et évolution chimique de la Voie lactée, analyse de grands volumes de données astronomiques.
- **Informatique** : calcul scientifique, pipelines de données, apprentissage automatique en astronomie, développement open-source.
- **Psychanalyse** :

### 3️⃣ Troisième étape : explorer le contenu

> [!warning] Version française encore en préparation
> Le reste du contenu de ce site n'est pas encore traduit en français — il est disponible en [portugais](/pt-br/) (langue d'origine) et, en partie, en [anglais](/en/).

Pour naviguer dans mon travail, explorez les sections du site (en portugais/anglais) :

<div class="media-carousel">
  <a href="/pt-br/research" class="carousel-slide">
    <img src="/assets/illustrations/research.svg" alt="Recherche" />
    <div class="slide-caption">Recherche</div>
  </a>
  <a href="/pt-br/resource" class="carousel-slide">
    <img src="/assets/illustrations/resource.svg" alt="Ressources" />
    <div class="slide-caption">Ressources</div>
  </a>
  <a href="/pt-br/resource/engenharia-de-computação" class="carousel-slide">
    <img src="/assets/illustrations/classes.svg" alt="Matières" />
    <div class="slide-caption">Matières</div>
  </a>
  <a href="/pt-br/media" class="carousel-slide">
    <img src="/assets/febic2024/febic.jpeg" alt="Médias" />
    <div class="slide-caption">Médias</div>
  </a>
  <a href="/pt-br/projects" class="carousel-slide">
    <img src="/assets/illustrations/projects.svg" alt="Projets" />
    <div class="slide-caption">Projets</div>
  </a>
  <a href="/pt-br/blog" class="carousel-slide">
    <img src="/assets/illustrations/toolkit.svg" alt="Blog" />
    <div class="slide-caption">Blog</div>
  </a>
</div>

- [Recherche](pt-br/research/) — Découvrez mes projets actuels et publications.
- [Ressources](pt-br/resource/) — Matériaux, scripts et outils utiles que j'ai développés ou que j'utilise.
- [Matières](pt-br/resource/engenharia-de-computação/) — Mes notes et travaux universitaires.
- [Médias](pt-br/media/) — Participations à des événements, salons et présentations.
- [Projets](pt-br/projects/) — Outils et applications que je développe en dehors de la recherche académique.
- [Blog](pt-br/blog/) — Pensées éparses, tutoriels et réflexions sur le parcours de recherche.

Ce site est d'abord rédigé en **portugais (Brésil)** puis traduit en anglais au fil du temps — le français est la langue la plus récente à rejoindre le site, il reste donc beaucoup à traduire. Si vous avez remarqué quelque chose de manquant ou d'obsolète, vous pouvez ouvrir une [issue dans le dépôt](https://github.com/pedroiff0/page/issues), ou [cliquer ici pour en ouvrir une déjà pré-remplie à partir du modèle de traduction](https://github.com/pedroiff0/page/issues/new?template=traducao.yml).
