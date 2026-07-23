---
publish: true
title: Sobre Mim
created: 2026-07-18T14:50:18.601-03:00
---

> [!info] Bem-vindo(a)!
> Esta é sua página de partida! Aqui você encontra tudo que precisa saber para conhecer minha jornada, pesquisas e trabalhos. Leia na ordem sugerida para ter a melhor experiência possível. 😊

## 📚 Por onde começar?

### 1️⃣ Primeiro passo: Sobre mim

<img src="../assets/profilepic.jpeg" alt="Pedro Henrique" width="160" style="border-radius: 50%; float: right; margin-left: 1.5rem; margin-bottom: 1rem; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">

Sou Pedro Henrique, estudante de Engenharia de Computação no [Instituto Federal Fluminense](https://portal1.iff.edu.br/), em Bom Jesus do Itabapoana, no interior do Rio de Janeiro, Brasil. Desde 2022, venho construindo uma ponte entre **ciência da computação** e **astronomia**, trabalhando em projetos de pesquisa que exploram populações estelares e a estrutura da Via Láctea.

Minha paixão está na interseção entre **métodos computacionais** e **problemas astrofísicos**. Acredito que ferramentas de código aberto e fluxos de trabalho reprodutíveis são essenciais para avançar a ciência e torná-la mais acessível a todos.

### 🌐 Redes Sociais

Caso queira entrar em contato, mande um email!

- 💻 [GitHub](https://github.com/pedroiff0)
- 💼 [LinkedIn](https://www.linkedin.com/in/pedroiff0/)
- 📸 [Instagram](https://instagram.com/fckpeeh)
- 🔬 [ORCID](https://orcid.org/0009-0003-6724-4640)
- ✉️ [E-mail](mailto:pedroiff0@gmail.com)

### 📬 Fale comigo

Prefere não abrir o seu programa de e-mail? Preencha os campos abaixo e a mensagem cai direto na minha caixa de entrada.

<form id="contact-form" class="contact-form">
  <input type="text" name="from_name" placeholder="Seu nome" required>
  <input type="email" name="reply_to" placeholder="Seu e-mail" required>
  <textarea name="message" placeholder="Sua mensagem" rows="5" required></textarea>
  <button type="submit">Enviar</button>
  <p id="contact-form-status"></p>
</form>

<script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js"></script>
<script>
(function() {
  // TODO(Pedro): substitua pelas suas credenciais de https://dashboard.emailjs.com
  // (crie uma conta grátis, um Email Service e um Email Template com as variáveis
  // from_name / reply_to / message usadas no formulário acima).
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
      status.textContent = "Formulário ainda não configurado — envie por e-mail direto por enquanto.";
      return;
    }
    status.textContent = "Enviando…";
    emailjs.sendForm(EMAILJS_SERVICE_ID, EMAILJS_TEMPLATE_ID, form).then(
      function() {
        status.textContent = "Mensagem enviada — obrigado pelo contato!";
        form.reset();
      },
      function(err) {
        status.textContent = "Não deu pra enviar agora. Tenta de novo ou manda um e-mail direto.";
      }
    );
  });
})();
</script>

### 2️⃣ Segundo passo: Áreas de Interesse

- **Astrofísica**: Arqueologia galáctica, populações estelares, estrutura e evolução química da Via Láctea, análise de grandes volumes de dados astronômicos.
- **Ciência da Computação**: Computação científica, pipelines de dados, aprendizado de máquina em astronomia, desenvolvimento open-source.
- **Psicanálise**:

### 3️⃣ Terceiro passo: Explorar o conteúdo

Para navegar pelo meu trabalho, explore as seções deste site:

<div class="media-carousel">
  <a href="/pt-br/research" class="carousel-slide">
    <img src="/assets/illustrations/research.svg" alt="Pesquisa" />
    <div class="slide-caption">Pesquisa</div>
  </a>
  <a href="/pt-br/resource" class="carousel-slide">
    <img src="/assets/illustrations/resource.svg" alt="Recursos" />
    <div class="slide-caption">Recursos</div>
  </a>
  <a href="/pt-br/resource/engenharia-de-computação" class="carousel-slide">
    <img src="/assets/illustrations/classes.svg" alt="Disciplinas" />
    <div class="slide-caption">Disciplinas</div>
  </a>
  <a href="/pt-br/media" class="carousel-slide">
    <img src="/assets/febic2024/febic.jpeg" alt="Mídia" />
    <div class="slide-caption">Mídia</div>
  </a>
  <a href="/pt-br/projects" class="carousel-slide">
    <img src="/assets/illustrations/projects.svg" alt="Projetos" />
    <div class="slide-caption">Projetos</div>
  </a>
  <a href="/pt-br/blog" class="carousel-slide">
    <img src="/assets/illustrations/toolkit.svg" alt="Blog" />
    <div class="slide-caption">Blog</div>
  </a>
</div>

- [Pesquisa](pt-br/research/) — Conheça meus projetos atuais.
- [Recursos](pt-br/resource/) — Materiais, scripts e ferramentas úteis que desenvolvi ou utilizo.
- [Disciplinas](pt-br/resource/engenharia-de-computação/) — Minhas anotações e trabalhos de faculdade.
- [Mídia](pt-br/media/) — Participações em eventos, feiras e apresentações.
- [Projetos](pt-br/projects/) — Ferramentas e aplicações que desenvolvo fora da pesquisa acadêmica.
- [Blog](pt-br/blog/) — Pensamentos aleatórios, tutoriais e reflexões sobre a jornada de pesquisa.

O enfoque deste site é ser um grande repositório de informações minhas. Ele está disponível em dois idiomas: todo o conteúdo é escrito primeiro em **Português (Brasil)** e traduzido para o inglês assim que possível — por isso, nem todas as páginas têm uma versão em inglês ainda.

Se você notou algo sem tradução (ou traduzido de forma desatualizada), pode abrir uma [issue no repositório](https://github.com/pedroiff0/page/issues) contando o que falta, ou [clicar aqui para abrir uma já preenchida a partir do template de tradução](https://github.com/pedroiff0/page/issues/new?template=traducao.yml).