import { h } from "preact";
import fs from "node:fs";
import path from "node:path";
import { slugifyFilePath } from "@quartz-community/utils/path";

const IMAGE_RE = /\.(jpe?g|png|webp|gif|avif)$/i;

function PhotoCarouselConstructor() {
  const PhotoCarousel = (props) => {
    const frontmatter = props?.fileData?.frontmatter ?? {};
    const folder = frontmatter.photoFolder;
    if (!folder || typeof folder !== "string") return null;

    const dir = path.join(process.cwd(), "content", "assets", "photos", folder);
    let files = [];
    try {
      files = fs
        .readdirSync(dir)
        .filter((f) => IMAGE_RE.test(f))
        .sort();
    } catch {
      return null;
    }
    if (files.length === 0) return null;

    const title = typeof frontmatter.title === "string" ? frontmatter.title : "";

    return h(
      "div",
      { class: "media-carousel" },
      files.map((f) => {
        // The Assets emitter slugifies every static file it copies (lowercase, etc.) —
        // mirror that here so hrefs match what actually lands in `public/`.
        const url = "/" + slugifyFilePath(`assets/photos/${folder}/${f}`);
        return h(
          "a",
          {
            href: url,
            class: "carousel-slide",
            target: "_blank",
            rel: "noopener",
          },
          h("img", { src: url, alt: title, loading: "lazy" }),
        );
      }),
    );
  };
  return PhotoCarousel;
}

export { PhotoCarouselConstructor as PhotoCarousel };
