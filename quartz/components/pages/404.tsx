import { i18n } from "../../i18n"
import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "../types"

const NotFound: QuartzComponent = ({ cfg, ctx }: QuartzComponentProps) => {
  const url = new URL(`https://${cfg.baseUrl ?? "example.com"}`)
  const baseDir = ctx.argv.serve ? "/" : url.pathname

  return (
    <article class="popover-hint">
      <h1>404</h1>
      <p>{i18n(cfg.locale).pages.error.notFound}</p>
      <a href={baseDir}>{i18n(cfg.locale).pages.error.home}</a>
      <script
        dangerouslySetInnerHTML={{
          __html: `
          if (typeof fetchData !== "undefined") {
            fetchData.then(function(index) {
              var basePath = document.body.dataset.basepath || "";
              if (basePath.length > 1 && basePath.endsWith("/")) {
                basePath = basePath.slice(0, -1);
              }
              var pathname = window.location.pathname;
              var hasBasePrefix = basePath.length > 1 && pathname.startsWith(basePath);
              if (hasBasePrefix) {
                pathname = pathname.slice(basePath.length);
              }
              if (pathname.startsWith("/")) {
                pathname = pathname.slice(1);
              }
              if (pathname.endsWith("/")) {
                pathname = pathname.slice(0, -1);
              }
              if (pathname.endsWith(".html")) {
                pathname = pathname.slice(0, -5);
              }
              if (pathname.endsWith("/index")) {
                pathname = pathname.slice(0, -6);
              }
              var lowered = pathname.toLowerCase();
              if (lowered !== pathname && index[lowered] != null) {
                var prefix = hasBasePrefix ? basePath : "";
                var target = prefix + (prefix.endsWith("/") ? "" : "/") + lowered;
                window.location.replace(target);
                return;
              }

              // --- pagina de traducao ausente ---
              var langs = ["pt-br", "en", "es", "fr"];
              var langIdx = langs.findIndex(function(l){ return pathname.startsWith(l + "/"); });
              if (langIdx !== -1) {
                var lang = langs[langIdx];
                var rest = pathname.slice(lang.length + 1);
                var msgs = {
                  "pt-br": "Oops, não foi possível obter a tradução para você. Sinto muito... Em breve estará traduzida!",
                  "en": "Oops, we couldn't find the translation for you. I'm sorry... It will be translated soon!",
                  "es": "Ups, no pudimos encontrar la traducción para ti. Lo siento... ¡Pronto estará traducida!",
                  "fr": "Oups, nous n'avons pas trouvé la traduction pour vous. Désolé... Elle sera bientôt traduite !"
                };
                var p = document.querySelector('p');
                if (p) p.textContent = msgs[lang] || msgs["en"];

                // link para abrir issue pedindo a traducao (pre-preenchido)
                var repo = "pedroiff0/page";
                var title = encodeURIComponent("Tradução em falta: " + pathname);
                var body = encodeURIComponent(
                  "A página \`" + pathname + "\` foi acessada mas ainda não tem tradução para \`" + lang + "\`.\n" +
                  "Por favor, adicione a tradução desta página (espelhar o slug em \`" + lang + "/\`)."
                );
                var issueUrl = "https://github.com/" + repo + "/issues/new?title=" + title + "&body=" + body + "&labels=translation";
                var a = document.createElement("a");
                a.href = issueUrl;
                a.target = "_blank";
                a.rel = "noopener";
                a.textContent = (lang === "pt-br") ? "Pedir esta tradução (abrir issue)" :
                               (lang === "en") ? "Request this translation (open issue)" :
                               (lang === "es") ? "Solicitar esta traducción (abrir issue)" :
                               "Demander cette traduction (ouvrir un issue)";
                a.style.display = "inline-block";
                a.style.marginTop = "0.8rem";
                if (p && p.parentNode) p.parentNode.insertBefore(a, p.nextSibling);

                // redireciona para o pt-br equivalente apos 5s (se existir)
                var ptTarget = (hasBasePrefix ? basePath : "") + "/pt-br/" + rest;
                var exists = index[ptTarget.toLowerCase()] != null || index["pt-br/" + rest.toLowerCase()] != null;
                if (exists) {
                  setTimeout(function () {
                    var msg2 = (lang === "pt-br") ? "Redirecionando para a versão em português..." :
                               (lang === "en") ? "Redirecting to the Portuguese version..." :
                               (lang === "es") ? "Redirigiendo a la versión en portugués..." :
                               "Redirection vers la version portugaise...";
                    if (p) p.textContent = msg2;
                    window.location.replace(ptTarget);
                  }, 5000);
                }
              }
            });
          }
          `,
        }}
      />
    </article>
  )
}

export default (() => NotFound) satisfies QuartzComponentConstructor
