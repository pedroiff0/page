import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { Date as DateComponent } from "./Date"
import { i18n } from "../i18n"
import { classNames } from "../util/lang"

const CreatedDate: QuartzComponent = ({ fileData, cfg, displayClass }: QuartzComponentProps) => {
  const created = fileData.dates?.created
  if (!created) return null
  const locale = cfg.locale ?? "en-US"

  return (
    <p class={classNames(displayClass, "created-date")}>
      {i18n(locale).components.contentMeta.created}: <DateComponent date={created} locale={locale} />
    </p>
  )
}

export default (() => CreatedDate) satisfies QuartzComponentConstructor
