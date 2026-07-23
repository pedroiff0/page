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
              
              if (pathname.startsWith("pt-br/") || pathname.startsWith("en/") || pathname.startsWith("es/") || pathname.startsWith("fr/")) {
                var msg;
                if (pathname.startsWith("pt-br/")) {
                  msg = "Oops, não foi possível obter a tradução para você. Sinto muito.... Em breve estará traduzido!";
                } else if (pathname.startsWith("es/")) {
                  msg = "Ups, no pudimos encontrar la traducción para ti. Lo siento... ¡Pronto estará traducida!";
                } else if (pathname.startsWith("fr/")) {
                  msg = "Oups, nous n'avons pas trouvé la traduction pour vous. Désolé... Elle sera bientôt traduite !";
                } else {
                  msg = "Oops, we couldn't find the translation for you. I'm sorry... It will be translated soon!";
                }
                var p = document.querySelector('p');
                if (p) p.textContent = msg;
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
