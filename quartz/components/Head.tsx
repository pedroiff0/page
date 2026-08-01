import { i18n } from "../i18n"
import { FullSlug, getFileExtension, joinSegments, pathToRoot } from "../util/path"
import { CSSResourceToStyleElement, JSResourceToScriptElement } from "../util/resources"
import { googleFontHref, googleFontSubsetHref } from "../util/theme"
import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { unescapeHTML } from "../util/escape"
import { CustomOgImagesEmitterName } from "../../.quartz/plugins"
export default (() => {
  const Head: QuartzComponent = ({
    cfg,
    fileData,
    externalResources,
    ctx,
  }: QuartzComponentProps) => {
    const titleSuffix = cfg.pageTitleSuffix ?? ""
    const title =
      (fileData.frontmatter?.title ?? i18n(cfg.locale).propertyDefaults.title) + titleSuffix
    const description =
      fileData.frontmatter?.socialDescription ??
      fileData.frontmatter?.description ??
      unescapeHTML(fileData.description?.trim() ?? i18n(cfg.locale).propertyDefaults.description)

    const { css, js, additionalHead } = externalResources

    const url = new URL(`https://${cfg.baseUrl ?? "example.com"}`)
    const path = url.pathname as FullSlug
    const baseDir = fileData.slug === "404" ? path : pathToRoot(fileData.slug!)
    const iconPath = joinSegments(baseDir, "static/icon.png")

    // Url of current page
    const socialUrl =
      fileData.slug === "404" ? url.toString() : joinSegments(url.toString(), fileData.slug!)

    const usesCustomOgImage = ctx.cfg.plugins.emitters.some(
      (e) => e.name === CustomOgImagesEmitterName,
    )
    const ogImageDefaultPath = `https://${cfg.baseUrl}/static/og-image.png`

    const coreStylesheet = css[0]?.content
    const coreScript = js.find(
      (r) => r.loadTime === "beforeDOMReady" && r.contentType === "external",
    )

    return (
      <head>
        <title>{title}</title>
        <meta charSet="utf-8" />
        {coreStylesheet && <link rel="preload" href={coreStylesheet} as="style" />}
        {coreScript && coreScript.contentType === "external" && (
          <link rel="preload" href={coreScript.src} as="script" />
        )}
        {cfg.theme.cdnCaching && cfg.theme.fontOrigin === "googleFonts" && (
          <>
            <link rel="preconnect" href="https://fonts.googleapis.com" />
            <link rel="preconnect" href="https://fonts.gstatic.com" />
            <link rel="stylesheet" href={googleFontHref(cfg.theme)} />
            {cfg.theme.typography.title && (
              <link rel="stylesheet" href={googleFontSubsetHref(cfg.theme, cfg.pageTitle)} />
            )}
          </>
        )}
        <link rel="preconnect" href="https://cdnjs.cloudflare.com" crossOrigin="anonymous" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />

        <meta name="og:site_name" content={cfg.pageTitle}></meta>
        <meta property="og:title" content={title} />
        <meta property="og:type" content="website" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content={title} />
        <meta name="twitter:description" content={description} />
        <meta property="og:description" content={description} />
        <meta property="og:image:alt" content={description} />

        {!usesCustomOgImage && (
          <>
            <meta property="og:image" content={ogImageDefaultPath} />
            <meta property="og:image:url" content={ogImageDefaultPath} />
            <meta name="twitter:image" content={ogImageDefaultPath} />
            <meta
              property="og:image:type"
              content={`image/${getFileExtension(ogImageDefaultPath) ?? "png"}`}
            />
          </>
        )}

        {cfg.baseUrl && (
          <>
            <meta property="twitter:domain" content={cfg.baseUrl}></meta>
            <meta property="og:url" content={socialUrl}></meta>
            <meta property="twitter:url" content={socialUrl}></meta>
          </>
        )}

        <link rel="icon" href={iconPath} />
        <meta name="description" content={description} />
        <meta name="generator" content="Quartz" />

        {css.map((resource) => CSSResourceToStyleElement(resource, true))}
        {js
          .filter((resource) => resource.loadTime === "beforeDOMReady")
          .map((res) => JSResourceToScriptElement(res, true))}
        {additionalHead.map((resource) => {
          if (typeof resource === "function") {
            return resource(fileData)
          } else {
            return resource
          }
        })}
        <script dangerouslySetInnerHTML={{ __html: `
          (function() {
            function initBackground() {
              if (document.getElementById("cosmic-bg")) return;
              
              const container = document.createElement("div");
              container.id = "cosmic-bg";
              container.style.position = "fixed";
              container.style.top = "0";
              container.style.left = "0";
              container.style.width = "100vw";
              container.style.height = "100vh";
              container.style.zIndex = "-1";
              container.style.pointerEvents = "none";
              container.style.overflow = "hidden";
              
              container.innerHTML = \`
                <div id="cosmic-image" style="
                  width: 110%;
                  height: 110%;
                  position: absolute;
                  top: -5%;
                  left: -5%;
                  background-image: url('/static/cosmic_bg_atual.png');
                  background-size: cover;
                  background-position: center;
                  transition: transform 0.2s ease-out, opacity 0.5s ease;
                "></div>
              \`;
              document.body.insertBefore(container, document.body.firstChild);
              
              function updateOpacity() {
                const img = document.getElementById("cosmic-image");
                if (!img) return;
                const isDark = document.documentElement.getAttribute("saved-theme") === "dark" || document.documentElement.dataset.theme === "dark";
                img.style.opacity = isDark ? "0.35" : "0.15";
              }
              
              updateOpacity();
              
              const themeObserver = new MutationObserver((mutations) => {
                mutations.forEach((mutation) => {
                  if (mutation.attributeName === "saved-theme" || mutation.attributeName === "data-theme") {
                    updateOpacity();
                  }
                });
              });
              themeObserver.observe(document.documentElement, { attributes: true });
              
              window.addEventListener("mousemove", (e) => {
                const img = document.getElementById("cosmic-image");
                if (!img) return;
                
                const dx = (e.clientX / window.innerWidth) - 0.5;
                const dy = (e.clientY / window.innerHeight) - 0.5;
                
                img.style.transform = "translate(" + (dx * 18) + "px, " + (dy * 18) + "px)";
              });
            }
            
            if (document.readyState === "loading") {
              document.addEventListener("DOMContentLoaded", initBackground);
            } else {
              initBackground();
            }
            document.addEventListener("nav", initBackground);
          })();
        ` }} />
      </head>
    )
  }

  return Head
}) satisfies QuartzComponentConstructor
