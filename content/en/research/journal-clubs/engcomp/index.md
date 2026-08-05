---
publish: true
title: "ENGCOMP"
created: 2026-07-26
modified: 2026-08-01
published: 2026-08-01T20:04:04.327-03:00
---

> [!note] Summary
> Journal club de **Computer Engineering** of the IFF Campus Bom Jesus do Itabapoana: we choose a recent article from the arXiv, someone presents, and the rest of the conversation is to discuss what was read. This page saves what has already been discussed [topics followed](en/research/journal-clubs/engcomp/topicos) show you where to look for the next one.

## 👥 Join

 The whole organization happens in the email group **[engcompbji](https://groups.google.com/g/engcompbji)** — that's where the call comes from each meeting, the article of the week and who presents it.

- ** Enter the group** —[subscribe by email](mailto:engcompbji+subscribe@googlegroups.com)(just send blank message) or [group on Google Groups](https://groups.google.com/g/engcompbji).
- ** Suggesting an article** — anyone in the group can indicate reading, does not need to be the one to present.
- ** Present** — 20 minutes are enough. The point is the discussion later, not the class.

 <a class="jc-button" href="mailto:engcompbji@googleggroups.com?subject=Sugest%C3%A3%20%20by%20article%20%E2%80%94%20Journal%20Club%20ENGCOMP&body=T%C3%ADtulum%3A%0%0ALink%20%20arXiv%3A%0%0AT%C3%C3peak%20%28ex.%3A%20cs.SE%29%3A%0%0A%0A%20val%20discuss%20%28two%20%20%C3%A%20line%29%3A%0A%0A

## 📚 Articles already discussed

 The table is generated from the frontmatter of the notes themselves in this folder — a new note appears on the next build alone without editing this page. View [default of each input](pt-br/research/journal-clubs#padrão-de-cada-entrada).

 '`base
 filters:
 and:
 'file.folder.startsWith("pt-br/research/journal-clubs/engcomp")'
 Only article notes have `arxiv`; it is what separates an entry from the pages
 support of this folder (index, topics, dashboard).
 note.arxiv
 formulas:
 article: 'link(file.path, note.title)'
 properties:
 formula. article:
 displayName: Article
 note. presenter:
 displayName: Presented
 note. authors:
 displayName: Author
 note.year:
 displayName: Year
 note. discussed:
 displayName: Discussion in
 It's okay The URL of arXiv enters as text and the Quartz turns it into external link
 Alone. Do not use link() here: it only solves internal path and transforms
 a URL in "../../https/arxiv.org/...". html() also does not serve — markup
 is escaped before reaching the cell.
 note. arxiv:
 displayName: arXiv
 views:
 type: table
 name: Articles discussed
 order:
 formula. article
 notice. host
 notice. authors
 notice. year
 notice. discussed
 notice. arxiv
 sort:
 property: note. discussed
 direction:
 '``

## 📣 Call for group

 Text ready to announce the next meeting. Copy, fill in the two gaps and send them to the group.

 <div class="jc-digest">
 <pre id="jc-digest-text">People, next meeting of the Computer Engineering Journal Club.

📅 When:
📄 Article: \[TITLE + ARXIV LINK]

 Anyone who wants to suggest reading for the next few weeks, the topics we follow are here:
 https://www.phrantrade.com/en-br/research/journal-clubs/engcomp/topicos

 The history of what we discussed is:
 https://www.phrantrade.com/en-br/research/journal-clubs/engcomp

 Until then!</pre> <button type="button" class="jc-button" id="jc-digest-copy">

 </div>

 <script>
 (function() {
 var btn = document.getElementById("jc-digest-copy");
 var pre = document.getElementById("jc-digest-text");
 if (!btn ;
 btn.addEventListener("click", function() {
 navigator.clipboard.writeText(pre.textContent).then(
 function() {
 btn.textContent = ";
 setTimeout(function() {btn.textContent = ";
 },
 function() {
 btn.textContent = "Didn't -- Copy manually";
 }
 );
 });
 })();
 </script>

 ---

## 🔗 References and correlations

- [Topics and where to look](en/research/journal-clubs/engcomp/topicos)— the categories of the arXiv which the club accompanies.
- [Club Dashboard](en/research/journal-clubs/engcomp/dashboard)— activity per month, topic and presenter.
- [Journal Clubs — Overview](en/research/journal-clubs)
- [MWBR](en/research/journal-clubs/mwbr)
- [Research — Overview](en/research)

> [!abstract] Automatic translation notice
> This page was automatically translated from Portuguese using the LibreTranslate-based automated translator implemented in `tools/translate_quartz.py` (it preserves wikilinks, embeds and proper names via positional splitting). Machine translation may contain inaccuracies — the original Portuguese version is the authoritative source.
