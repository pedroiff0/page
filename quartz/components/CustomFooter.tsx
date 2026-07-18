import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { classNames } from "../util/lang"

const CustomFooter: QuartzComponent = ({ displayClass, fileData }: QuartzComponentProps) => {
  const year = new Date().getFullYear()
  const isEn = fileData.slug?.startsWith("en") ?? false
  
  const content = {
    title: "Pedro Henrique Rocha de Andrade",
    subtitle: isEn ? "Computer Engineering Student" : "Estudante de Engenharia de Computação",
    location: isEn ? "📍 Rio de Janeiro, Brazil" : "📍 Rio de Janeiro, Brasil",
    institution: "🏛️ Instituto Federal Fluminense",
    email: "✉️ pedroiff0@gmail.com",
    linksTitle: isEn ? "Useful Links" : "Links Úteis",
    builtWith: isEn ? "Built with" : "Construído com"
  }

  return (
    <footer class={classNames(displayClass, "custom-footer")} style={{ marginTop: "2rem", textAlign: "center" }}>
      <hr />
      <p style={{ margin: "1rem 0" }}>© {year} Pedro H. R. de Andrade. {content.builtWith} <a href="https://quartz.jzhao.xyz/" target="_blank">Quartz</a>.</p>
    </footer>
  )
}



export default (() => CustomFooter) satisfies QuartzComponentConstructor
