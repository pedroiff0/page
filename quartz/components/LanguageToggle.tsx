import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { classNames } from "../util/lang"

const LanguageToggle: QuartzComponent = ({ displayClass }: QuartzComponentProps) => {
  return (
    <div class={classNames(displayClass, "nav-lang")}>
      <a href="/en/" title="English" data-lang="en" onclick="event.preventDefault(); window.location.href = window.translatePath(window.location.pathname, 'en')">🇺🇸 EN</a>
      <a href="/pt-br/" title="Português" data-lang="pt-br" onclick="event.preventDefault(); window.location.href = window.translatePath(window.location.pathname, 'pt-br')">🇧🇷 PT</a>
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
              if (path === '/' || path === '') return '/' + targetLang + '/';
              const parts = path.split('/').filter(p => p);
              if (parts.length === 0) return '/' + targetLang + '/';
              
              // Replace language root
              if (parts[0] === 'pt-br' || parts[0] === 'en') {
                parts[0] = targetLang;
              } else {
                parts.unshift(targetLang);
              }
              
              // Replace first folder if it exists in dictionary
              if (parts.length > 1 && window.langDict[parts[1]]) {
                parts[1] = window.langDict[parts[1]];
              }
              
              return '/' + parts.join('/') + '/';
            };
          }
        `
      }} />
    </div>
  )
}



export default (() => LanguageToggle) satisfies QuartzComponentConstructor
