---
publish: true
title: "arXiv Searcher"
created: 2026-03-13
---

> [!note] In one line
> A tool, in **planning**, to automatically search and organize arXiv papers by subject/keyword.

Designed to run as a daemon (possibly dockerized), polling the arXiv API on a schedule and generating:

- A daily **Markdown** digest: table with date, title, first author, subject and arXiv link.
- **Ready-to-use LaTeX citations**, matching the reference style already used in my papers.
- Configuration via `.csv` spreadsheet — default search subject configurable, with a one-off keyword search option that doesn't touch that config.

Similar open projects I'm using as inspiration: [biblio.el](https://github.com/cpitclaudel/biblio.el), [bibcure](https://github.com/bibcure/bibcure) and [dailyarxiv](https://dailyarxiv.com).

**Status:** in planning — data structure (Markdown/LaTeX) and configuration menu (default subject via cronjob, manual subject choice, or subject+keyword combination) already sketched out.
