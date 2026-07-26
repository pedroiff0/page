import { h } from "preact";
import fs from "node:fs";
import path from "node:path";
import { slugifyFilePath, resolveRelative } from "@quartz-community/utils/path";

const IMAGE_RE = /\.(jpe?g|png|webp|gif|avif)$/i;

function listPhotos(folder) {
  const dir = path.join(process.cwd(), "content", "assets", "photos", folder);
  try {
    return fs
      .readdirSync(dir)
      .filter((f) => IMAGE_RE.test(f))
      .sort();
  } catch {
    return [];
  }
}

// The Assets emitter slugifies every static file it copies (lowercase, etc.) —
// mirror that here so hrefs match what actually lands in `public/`.
function photoUrl(folder, file) {
  return "/" + slugifyFilePath(`assets/photos/${folder}/${file}`);
}

function slide(href, imgSrc, alt, caption) {
  return h(
    "a",
    { href, class: "carousel-slide" },
    imgSrc ? h("img", { src: imgSrc, alt, loading: "lazy" }) : null,
    caption ? h("div", { class: "slide-caption" }, caption) : null,
  );
}

function PhotoCarouselConstructor() {
  const PhotoCarousel = (props) => {
    const fileData = props?.fileData ?? {};
    const frontmatter = fileData.frontmatter ?? {};
    const folder = frontmatter.photoFolder;

    // Mode 1: this note itself declares a photoFolder — show every photo in it,
    // opening the full-size image directly (existing single-event behaviour).
    if (folder && typeof folder === "string") {
      const files = listPhotos(folder);
      if (files.length === 0) return null;
      const title = typeof frontmatter.title === "string" ? frontmatter.title : "";
      return h(
        "div",
        { class: "media-carousel" },
        files.map((f) => {
          const url = photoUrl(folder, f);
          return h(
            "a",
            { href: url, class: "carousel-slide", target: "_blank", rel: "noopener" },
            h("img", { src: url, alt: title, loading: "lazy" }),
          );
        }),
      );
    }

    // Mode 2: this is a folder-index note (e.g. media/index.md, media/2025/index.md).
    // Gather every descendant note that DOES declare a photoFolder and build one
    // slide per event, linking to the note and using its first photo as thumbnail.
    // New event notes need zero manual carousel edits — they just show up here
    // once published, and start showing a real photo the moment one is added.
    const slug = fileData.slug;
    if (!slug || slug === "index" || !slug.endsWith("/index")) return null;

    const prefix = slug.slice(0, -"/index".length);
    // Scope the gallery to the "media" section specifically (any language) —
    // otherwise a broad index page like the homepage would also match, since
    // it technically sits above every media note in the slug tree too.
    if (!prefix.split("/").includes("media")) return null;

    const allFiles = props?.allFiles ?? [];
    const children = allFiles.filter((f) => {
      const s = f.slug;
      if (!s || !s.startsWith(prefix + "/")) return false;
      const childFolder = f.frontmatter?.photoFolder;
      return typeof childFolder === "string" && childFolder.length > 0;
    });
    if (children.length === 0) return null;

    children.sort((a, b) => {
      const da = a.frontmatter?.created ? new Date(a.frontmatter.created).getTime() : 0;
      const db = b.frontmatter?.created ? new Date(b.frontmatter.created).getTime() : 0;
      return da - db;
    });

    return h(
      "div",
      { class: "media-carousel" },
      children.map((child) => {
        const childFolder = child.frontmatter.photoFolder;
        const title = typeof child.frontmatter?.title === "string" ? child.frontmatter.title : "";
        const files = listPhotos(childFolder);
        const imgSrc = files.length > 0 ? photoUrl(childFolder, files[0]) : null;
        const href = resolveRelative(slug, child.slug);
        return slide(href, imgSrc, title, title);
      }),
    );
  };
  return PhotoCarousel;
}

export { PhotoCarouselConstructor as PhotoCarousel };
