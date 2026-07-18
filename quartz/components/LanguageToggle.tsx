import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { classNames } from "../util/lang"

const LanguageToggle: QuartzComponent = ({ displayClass, cfg }: QuartzComponentProps) => {
  const basePath = cfg.baseUrl ? "/" + cfg.baseUrl.split("/").slice(1).join("/") : ""

  return (
    <div class={classNames(displayClass, "nav-lang")}>
      <a href={`${basePath}/en/`} title="English" data-lang="en" data-router-ignore onclick="event.preventDefault(); window.location.href = window.translatePath(window.location.pathname, 'en')">🇺🇸 EN</a>
      <a href={`${basePath}/pt-br/`} title="Português" data-lang="pt-br" data-router-ignore onclick="event.preventDefault(); window.location.href = window.translatePath(window.location.pathname, 'pt-br')">🇧🇷 PT</a>
      <script dangerouslySetInnerHTML={{
        __html: `
          if (!window.translatePath) {
            window.langDict = {
              'pt-br': 'en', 'en': 'pt-br',
              'pesquisa': 'research', 'research': 'pesquisa',
              'recursos': 'resource', 'resource': 'recursos',
              'disciplinas': 'classes', 'classes': 'disciplinas',
              'midia': 'media', 'media': 'midia',
              'publicacoes': 'publications', 'publications': 'publicacoes'
            };

            window.translatePath = function(path, targetLang) {
              const parts = path.split('/').filter(p => p);
              const langIdx = parts.findIndex(p => p === 'en' || p === 'pt-br');

              // Everything before the language segment is the base path (e.g. GitHub Pages project prefix)
              const prefix = langIdx === -1 ? parts : parts.slice(0, langIdx);
              const rest = langIdx === -1 ? [] : parts.slice(langIdx + 1);

              // Translate the first folder after the language segment, if it has a known counterpart
              if (rest.length > 0 && window.langDict[rest[0]]) {
                rest[0] = window.langDict[rest[0]];
              }

              return '/' + [...prefix, targetLang, ...rest].join('/') + '/';
            };
          }
        `
      }} />
    </div>
  )
}



export default (() => LanguageToggle) satisfies QuartzComponentConstructor
