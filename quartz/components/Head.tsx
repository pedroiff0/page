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
                      <feGaussianBlur stdDeviation="30" result="blur" />
                      <feComposite in="SourceGraphic" in2="blur" operator="over" />
                    </filter>
                    
                    <linearGradient id="starStream" x1="0%" y1="0%" x2="100%" y2="100%">
                      <stop offset="0%" stop-color="#1e3a8a" stop-opacity="0.2" />
                      <stop offset="30%" stop-color="#1d4ed8" stop-opacity="0.3" />
                      <stop offset="60%" stop-color="#eab308" stop-opacity="0.25" />
                      <stop offset="100%" stop-color="#3b82f6" stop-opacity="0.15" />
                    </linearGradient>
                  </defs>

                  <g id="cosmic-group" opacity="0.03" style="transition: transform 0.2s ease-out, opacity 0.5s ease;">
                    <!-- 1. Colinas (Hills) -->
                    <path d="M-50,950 Q300,900 800,980 T1920,930 L1920,1080 L-50,1080 Z" fill="#0f172a" opacity="0.5" />
                    <path d="M-50,980 Q450,930 1100,1010 T1920,960 L1920,1080 L-50,1080 Z" fill="#020617" />

                    <!-- 2. O Fluxo de Vento Espiral (Swirling flows) -->
                    <path d="M-100,700 C300,650 500,300 960,540 C1420,780 1600,400 2020,300" fill="none" stroke="url(#starStream)" stroke-width="120" opacity="0.6" filter="url(#glow)" />
                    
                    <path d="M-100,700 C300,650 500,300 960,540 C1420,780 1600,400 2020,300" fill="none" stroke="#3b82f6" stroke-width="30" stroke-linecap="round" stroke-dasharray="15 45" opacity="0.5" />
                    <path d="M-100,720 C300,670 500,320 960,560 C1420,800 1600,420 2020,320" fill="none" stroke="#eab308" stroke-width="10" stroke-linecap="round" stroke-dasharray="10 30" opacity="0.6" />
                    <path d="M-100,680 C300,630 500,280 960,520 C1420,760 1600,380 2020,280" fill="none" stroke="#ffffff" stroke-width="6" stroke-linecap="round" stroke-dasharray="8 25" opacity="0.7" filter="url(#glow)" />
                    <path d="M-100,660 C300,610 500,260 960,500 C1420,740 1600,360 2020,260" fill="none" stroke="#1d4ed8" stroke-width="20" stroke-linecap="round" stroke-dasharray="12 40" opacity="0.4" />

                    <!-- Redemoinhos menores (Small swirls) -->
                    <path d="M820,460 A80,80 0 1,1 900,540 A50,50 0 1,1 870,510" fill="none" stroke="#eab308" stroke-width="8" stroke-linecap="round" stroke-dasharray="6 15" opacity="0.6" />
                    <path d="M1080,620 A90,90 0 1,0 990,530 A60,60 0 1,0 1020,560" fill="none" stroke="#60a5fa" stroke-width="6" stroke-linecap="round" stroke-dasharray="5 15" opacity="0.5" />

                    <!-- 3. A Lua Crescente (Crescent Moon) -->
                    <circle cx="1720" cy="180" r="120" fill="#fef08a" opacity="0.15" filter="url(#glow)" />
                    <circle cx="1720" cy="180" r="60" fill="#facc15" opacity="0.25" filter="url(#glow)" />
                    <path d="M1680,110 C1740,110 1790,150 1790,210 C1790,270 1730,310 1670,290 C1720,270 1750,220 1740,170 C1730,130 1700,120 1680,110 Z" fill="#facc15" opacity="0.95" filter="url(#glow)" />

                    <!-- 4. Estrelas com Halo (Stars with Halos) -->
                    <g class="cosmic-star" data-depth="0.3" style="transition: transform 0.2s ease-out;">
                      <circle cx="400" cy="300" r="60" fill="none" stroke="#fef08a" stroke-width="1.5" stroke-dasharray="3 15" opacity="0.3" />
                      <circle cx="400" cy="300" r="40" fill="none" stroke="#eab308" stroke-width="3" stroke-dasharray="4 10" opacity="0.5" />
                      <circle cx="400" cy="300" r="20" fill="none" stroke="#ffffff" stroke-width="4" stroke-dasharray="3 8" opacity="0.7" />
                      <circle cx="400" cy="300" r="12" fill="#fef08a" opacity="0.8" filter="url(#glow)" />
                      <circle cx="400" cy="300" r="4" fill="#ffffff" opacity="0.9" />
                    </g>

                    <g class="cosmic-star" data-depth="0.5" style="transition: transform 0.2s ease-out;">
                      <circle cx="1400" cy="650" r="70" fill="none" stroke="#fef08a" stroke-width="2" stroke-dasharray="4 16" opacity="0.3" />
                      <circle cx="1400" cy="650" r="45" fill="none" stroke="#eab308" stroke-width="3" stroke-dasharray="5 12" opacity="0.5" />
                      <circle cx="1400" cy="650" r="22" fill="none" stroke="#ffffff" stroke-width="4" stroke-dasharray="4 8" opacity="0.7" />
                      <circle cx="1400" cy="650" r="16" fill="#fef08a" opacity="0.7" filter="url(#glow)" />
                      <circle cx="1400" cy="650" r="5" fill="#ffffff" opacity="0.9" />
                    </g>

                    <g class="cosmic-star" data-depth="0.2" style="transition: transform 0.2s ease-out;">
                      <circle cx="750" cy="200" r="40" fill="none" stroke="#60a5fa" stroke-width="2" stroke-dasharray="3 10" opacity="0.4" />
                      <circle cx="750" cy="200" r="20" fill="none" stroke="#eab308" stroke-width="3" stroke-dasharray="4 8" opacity="0.6" />
                      <circle cx="750" cy="200" r="10" fill="#fef08a" opacity="0.7" filter="url(#glow)" />
                      <circle cx="750" cy="200" r="3" fill="#ffffff" opacity="0.9" />
                    </g>

                    <g class="cosmic-star" data-depth="0.4" style="transition: transform 0.2s ease-out;">
                      <circle cx="1150" cy="800" r="50" fill="none" stroke="#fef08a" stroke-width="2" stroke-dasharray="4 12" opacity="0.4" />
                      <circle cx="1150" cy="800" r="25" fill="none" stroke="#eab308" stroke-width="3" stroke-dasharray="3 8" opacity="0.6" />
                      <circle cx="1150" cy="800" r="12" fill="#fef08a" opacity="0.7" filter="url(#glow)" />
                      <circle cx="1150" cy="800" r="4" fill="#ffffff" opacity="0.9" />
                    </g>

                    <g class="cosmic-star" data-depth="0.3" style="transition: transform 0.2s ease-out;">
                      <circle cx="1350" cy="180" r="40" fill="none" stroke="#fef08a" stroke-width="1.5" stroke-dasharray="3 10" opacity="0.4" />
                      <circle cx="1350" cy="180" r="20" fill="#eab308" opacity="0.7" filter="url(#glow)" />
                      <circle cx="1350" cy="180" r="5" fill="#ffffff" opacity="0.9" />
                    </g>

                    <g class="cosmic-star" data-depth="0.4" style="transition: transform 0.2s ease-out;">
                      <circle cx="200" cy="750" r="40" fill="none" stroke="#60a5fa" stroke-width="2" stroke-dasharray="3 10" opacity="0.4" />
                      <circle cx="200" cy="750" r="18" fill="#eab308" opacity="0.6" filter="url(#glow)" />
                      <circle cx="200" cy="750" r="4" fill="#ffffff" opacity="0.9" />
                    </g>

                    <!-- 5. O Cipreste (Cypress) -->
                    <path d="M0,1080 L180,1080 C150,900 240,700 200,500 C165,370 120,250 80,180 C70,300 75,450 60,600 C40,750 10,900 0,1080 Z" fill="#020617" opacity="0.85" />
                    <path d="M0,1080 L150,1080 C120,930 200,750 170,550 C140,420 105,300 80,240 C75,320 70,470 55,620 C35,760 10,910 0,1080 Z" fill="#080e1e" />
                  </g>
                </svg>
              \`;
              document.body.insertBefore(container, document.body.firstChild);
              
              function updateOpacity() {
                const group = document.getElementById("cosmic-group");
                if (!group) return;
                const isDark = document.documentElement.getAttribute("saved-theme") === "dark" || document.documentElement.dataset.theme === "dark";
                group.setAttribute("opacity", isDark ? "0.035" : "0.015");
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
