import { h } from "preact";

// Content slugs are identical across locales (content/en/x mirrors
// content/pt-br/x), so the language of a page is just its first slug
// segment -- no separate translation lookup needed.
const TITLES = {
  "pt-br": "Bem-Vindo!",
  en: "Welcome!",
  es: "¡Bienvenido!",
  fr: "Bienvenue !",
};
const DEFAULT_TITLE = "Bem-Vindo! / Welcome!";

function pathToRoot(slug) {
  const rootPath = slug
    .split("/")
    .filter((x) => x !== "")
    .slice(0, -1)
    .map(() => "..")
    .join("/");
  return rootPath.length === 0 ? "." : rootPath;
}

function titleForSlug(slug, fallback) {
  const firstSegment = (slug || "").split("/")[0];
  return TITLES[firstSegment] ?? fallback;
}

function PageTitleConstructor() {
  const PageTitle = (props) => {
    const cfg = props?.cfg ?? {};
    const fileData = props?.fileData ?? {};
    const displayClass = props?.displayClass ?? "";
    const fallback = cfg.pageTitle ?? DEFAULT_TITLE;
    const title = titleForSlug(fileData.slug, fallback);
    const baseDir = pathToRoot(fileData.slug ?? "");
    const classes = ["page-title", displayClass].filter(Boolean).join(" ");
    return h("h2", { class: classes }, h("a", { href: baseDir }, title));
  };

  PageTitle.css = `
.page-title {
  font-size: 1.75rem;
  margin: 0;
  font-family: var(--titleFont);
}
`;

  return PageTitle;
}

export { PageTitleConstructor as PageTitle };
