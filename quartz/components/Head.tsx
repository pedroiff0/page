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
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="100%" height="100%" preserveAspectRatio="xMidYMid slice" style="background-color: transparent;">
                  <defs>
                    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
                      <feGaussianBlur stdDeviation="40" result="blur" />
                      <feComposite in="SourceGraphic" in2="blur" operator="over" />
                    </filter>
                    
                    <linearGradient id="starStream" x1="0%" y1="0%" x2="100%" y2="100%">
                      <stop offset="0%" stop-color="#4a6fa5" stop-opacity="0.15" />
                      <stop offset="30%" stop-color="#164e63" stop-opacity="0.25" />
                      <stop offset="60%" stop-color="#eab308" stop-opacity="0.2" />
                      <stop offset="100%" stop-color="#3b82f6" stop-opacity="0.1" />
                    </linearGradient>
                  </defs>

                  <g id="cosmic-group" opacity="0.03" filter="url(#glow)" style="transition: transform 0.2s ease-out, opacity 0.5s ease;">
                    <path d="M-100,700 C300,650 500,300 960,540 C1420,780 1600,400 2020,300 L2020,450 C1600,550 1420,930 960,690 C500,450 300,800 -100,850 Z" fill="url(#starStream)" />
                    
                    <path d="M100,550 Q450,250 850,480 T1700,400" fill="none" stroke="#60a5fa" stroke-width="40" stroke-linecap="round" stroke-dasharray="10 50" opacity="0.4" />
                    <path d="M200,600 Q550,350 950,580 T1800,500" fill="none" stroke="#fef08a" stroke-width="15" stroke-linecap="round" stroke-dasharray="5 30" opacity="0.6" />
                    <path d="M-50,620 Q300,400 750,520 T1600,450" fill="none" stroke="#1e3a8a" stroke-width="60" stroke-linecap="round" opacity="0.3" />

                    <circle cx="960" cy="540" r="250" fill="#fef08a" opacity="0.15" filter="url(#glow)" />
                    <circle cx="960" cy="540" r="120" fill="#ffffff" opacity="0.2" />

                    <path d="M850,450 A60,60 0 1,1 910,510 A40,40 0 1,1 890,490" fill="none" stroke="#eab308" stroke-width="8" stroke-linecap="round" opacity="0.5" />
                    <path d="M1050,600 A70,70 0 1,0 980,530 A50,50 0 1,0 1000,550" fill="none" stroke="#93c5fd" stroke-width="6" stroke-linecap="round" opacity="0.4" />

                    <circle class="cosmic-star" data-depth="0.3" cx="400" cy="300" r="15" fill="#fef08a" opacity="0.7" style="transition: transform 0.2s ease-out;" />
                    <circle class="cosmic-star" data-depth="0.3" cx="420" cy="280" r="4" fill="#ffffff" opacity="0.9" style="transition: transform 0.2s ease-out;" />
                    
                    <circle class="cosmic-star" data-depth="0.5" cx="1400" cy="700" r="25" fill="#fef08a" opacity="0.5" style="transition: transform 0.2s ease-out;" />
                    <circle class="cosmic-star" data-depth="0.5" cx="1400" cy="700" r="6" fill="#ffffff" opacity="0.8" style="transition: transform 0.2s ease-out;" />
                    
                    <circle class="cosmic-star" data-depth="0.2" cx="1650" cy="250" r="18" fill="#93c5fd" opacity="0.6" style="transition: transform 0.2s ease-out;" />
                    <circle class="cosmic-star" data-depth="0.4" cx="800" cy="750" r="12" fill="#fef08a" opacity="0.5" style="transition: transform 0.2s ease-out;" />
                  </g>
                </svg>
              \`;
              document.body.insertBefore(container, document.body.firstChild);
              
              function updateOpacity() {
                const group = document.getElementById("cosmic-group");
                if (!group) return;
                const isDark = document.documentElement.getAttribute("saved-theme") === "dark" || document.documentElement.dataset.theme === "dark";
                group.setAttribute("opacity", isDark ? "0.035" : "0.018");
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
                const group = document.getElementById("cosmic-group");
                if (!group) return;
                
                const dx = (e.clientX / window.innerWidth) - 0.5;
                const dy = (e.clientY / window.innerHeight) - 0.5;
                
                group.style.transform = "translate(" + (dx * 12) + "px, " + (dy * 12) + "px)";
                
                const stars = document.querySelectorAll(".cosmic-star");
                stars.forEach(star => {
                  const depth = parseFloat(star.getAttribute("data-depth") || "0.3");
                  const starShiftX = dx * 30 * depth;
                  const starShiftY = dy * 30 * depth;
                  star.style.transform = "translate(" + starShiftX + "px, " + starShiftY + "px)";
                  star.style.transformOrigin = star.getAttribute("cx") + "px " + star.getAttribute("cy") + "px";
                });
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
