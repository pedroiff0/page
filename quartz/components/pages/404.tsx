import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "../types"

const NotFound: QuartzComponent = ({ cfg, ctx }: QuartzComponentProps) => {
  const url = new URL(`https://${cfg.baseUrl ?? "example.com"}`)
  const baseDir = ctx.argv.serve ? "/" : url.pathname

  // textos por idioma (detectado da URL no cliente)
  const I18N = {
    pt: {
      title: "Página não encontrada",
      msg: "Ops! Não encontramos esta página. Ela pode ser privada ou ainda não foi traduzida para este idioma. Você pode solicitar a tradução abaixo.",
      home: "Voltar à página inicial",
      request: "Solicitar esta tradução",
      redirect: "Redirecionando para a versão em português…",
      issueTitle: "Tradução em falta: {{slug}}",
      issueBody: "A página `{{slug}}` foi acessada mas ainda não tem tradução para `{{lang}}`.\nPor favor, adicione a tradução desta página.",
    },
    en: {
      title: "Page not found",
      msg: "Oops! We couldn't find this page. It may be private or not translated into this language yet. You can request the translation below.",
      home: "Back to home page",
      request: "Request this translation",
      redirect: "Redirecting to the Portuguese version…",
      issueTitle: "Missing translation: {{slug}}",
      issueBody: "The page `{{slug}}` was accessed but has no translation into `{{lang}}` yet.\nPlease add the translation for this page.",
    },
    es: {
      title: "Página no encontrada",
      msg: "¡Ups! No encontramos esta página. Puede ser privada o no estar traducida a este idioma todavía. Puedes solicitar la traducción abajo.",
      home: "Volver a la página de inicio",
      request: "Solicitar esta traducción",
      redirect: "Redirigiendo a la versión en portugués…",
      issueTitle: "Traducción en falta: {{slug}}",
      issueBody: "La página `{{slug}}` fue accedida pero aún no tiene traducción a `{{lang}}`.\nPor favor, añade la traducción de esta página.",
    },
    fr: {
      title: "Page introuvable",
      msg: "Oups ! Nous n'avons pas trouvé cette page. Elle peut être privée ou pas encore traduite dans cette langue. Vous pouvez demander la traduction ci-dessous.",
      home: "Retour à l'accueil",
      request: "Demander cette traduction",
      redirect: "Redirection vers la version portugaise…",
      issueTitle: "Traduction manquante : {{slug}}",
      issueBody: "La page `{{slug}}` a été consultée mais n'a pas encore de traduction en `{{lang}}`.\nMerci d'ajouter la traduction de cette page.",
    },
  }

  return (
    <article class="notfound">
      <img
        class="notfound-gif"
        src="https://media.giphy.com/media/13CoXDiaCcCoyk/giphy.gif"
        alt="404"
        onError={(e) => {
          e.currentTarget.style.display = "none"
          const em = document.getElementById("nf-emoji")
          if (em) em.style.display = "block"
        }}
      />
      <div id="nf-emoji" class="notfound-emoji" style="display:none">👻</div>
      <h1 id="nf-title" data-default="404">404</h1>
      <p id="nf-msg">…</p>
      <a id="nf-home" class="notfound-btn" href={baseDir}>…</a>
      <a id="nf-issue" class="notfound-btn notfound-btn-secondary" href="#" target="_blank" rel="noopener">
        …
      </a>
      <script
        dangerouslySetInnerHTML={{
          __html: `
          (function(){
            var I18N = ${JSON.stringify(I18N)};
            function detectLang() {
              var p = window.location.pathname.replace(/^\\//, "");
              var langs = ["pt-br","en","es","fr"];
              var hit = langs.find(function(l){ return p === l || p.startsWith(l + "/"); });
              if (hit === "pt-br") return "pt";
              return hit || "pt";
            }
            var lang = detectLang();
            var T = I18N[lang] || I18N.pt;

            var titleEl = document.getElementById("nf-title");
            var msgEl = document.getElementById("nf-msg");
            var homeEl = document.getElementById("nf-home");
            var issueEl = document.getElementById("nf-issue");
            if (titleEl) titleEl.textContent = T.title;
            if (msgEl) msgEl.textContent = T.msg;
            if (homeEl) homeEl.textContent = T.home;
            if (issueEl) issueEl.textContent = T.request;

            // issue pre-preenchida pedindo a traducao da pagina acessada
            var basePath = document.body.dataset.basepath || "";
            if (basePath.length > 1 && basePath.endsWith("/")) basePath = basePath.slice(0,-1);
            var pathname = window.location.pathname;
            if (basePath.length > 1 && pathname.startsWith(basePath)) pathname = pathname.slice(basePath.length);
            var slug = pathname.replace(/^\//,"").replace(/\.html$/,"").replace(/\/index$/,"");
            var repo = "pedroiff0/page";
            var issueTitle = encodeURIComponent(
              T.issueTitle.replace("{{slug}}", slug).replace("{{lang}}", lang)
            );
            var issueBody = encodeURIComponent(
              T.issueBody.replace("{{slug}}", slug).replace("{{lang}}", lang)
            );
            if (issueEl) issueEl.href = "https://github.com/" + repo + "/issues/new?title=" + issueTitle + "&body=" + issueBody + "&labels=translation";

            // redirect para pt-br equivalente apos 5s (se existir)
            if (typeof fetchData !== "undefined") {
              fetchData.then(function(index){
                var rest = slug.replace(/^(pt-br|en|es|fr)\\/?/, "");
                var ptTarget = (basePath.length>1?basePath:"") + "/pt-br/" + rest;
                var exists = index[ptTarget.toLowerCase()] != null || index[("pt-br/"+rest).toLowerCase()] != null;
                if (exists) {
                  setTimeout(function(){
                    if (msgEl) msgEl.textContent = T.redirect;
                    window.location.replace(ptTarget);
                  }, 5000);
                }
              });
            }
          })();
          `,
        }}
      />
    </article>
  )
}

export default (() => NotFound) satisfies QuartzComponentConstructor
