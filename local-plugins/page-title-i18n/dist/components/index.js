import { h } from "preact";

// The site title is deliberately language-neutral -- a name, not a greeting --
// so there is nothing left to translate per locale: every page renders the
// same `pageTitle` from quartz.config.yaml. This component stays in place
// because it is what quartz.config.yaml registers in the PageTitle slot, and
// because it is where a per-locale title would go again if one is ever wanted:
// content slugs are identical across locales (content/en/x mirrors
// content/pt-br/x), so the language of a page is just its first slug segment
// -- key a lookup table on that, no translation dictionary needed.
const DEFAULT_TITLE = "Pedro H. R. de Andrade";

function pathToRoot(slug) {
  const rootPath = slug
    .split("/")
    .filter((x) => x !== "")
    .slice(0, -1)
    .map(() => "..")
    .join("/");
  return rootPath.length === 0 ? "." : rootPath;
}

function PageTitleConstructor() {
  const PageTitle = (props) => {
    const cfg = props?.cfg ?? {};
    const fileData = props?.fileData ?? {};
    const displayClass = props?.displayClass ?? "";
    const title = cfg.pageTitle ?? DEFAULT_TITLE;
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
