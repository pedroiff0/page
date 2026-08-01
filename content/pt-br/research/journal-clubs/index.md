---
publish: true
title: Journal Clubs
created: 2026-07-26
modified: 2026-07-26
---

> [!note] Resumo
> Lista curada dos artigos que já discuti em journal club, separada por grupo/área: **MWBR** (grupo de pesquisa em Via Láctea/arqueologia galáctica) e **ENGCOMP** (Engenharia de Computação). Cada entrada linka o artigo no arXiv e traz minha síntese da discussão — pontos levantados, críticas e conexões com outros trabalhos —, não o artigo completo.

Diferente de uma simples anotação de leitura individual, um Journal Club aqui é **um artigo que passou por discussão em grupo** — a nota registra também o que foi debatido, não só o conteúdo do artigo.

## Grupos

- **[MWBR](pt-br/research/journal-clubs/mwbr)** — grupo de pesquisa em Via Láctea, arqueologia galáctica e populações estelares.
- **[ENGCOMP](pt-br/research/journal-clubs/engcomp)** — journal club de Engenharia de Computação.

Cada uma dessas páginas monta a própria lista de artigos a partir do frontmatter das notas da pasta, via [Bases do Obsidian](https://help.obsidian.md/bases) — não há lista escrita à mão para manter em dia.

## Padrão de cada entrada

> [!example] Modelo de nota de artigo
> Toda nota de artigo discutido segue a mesma estrutura. Os quatro primeiros campos alimentam a tabela da página do grupo, que é gerada automaticamente — basta criar a nota na pasta certa (`mwbr/` ou `engcomp/`) e ela aparece sozinha no próximo build.
> ```markdown
> ---
> publish: true
> title: "Título curto do artigo"
> authors: "Sobrenome, A. et al."
> year: 2026
> arxiv: "https://arxiv.org/abs/XXXX.XXXXX"
> discutido: 2026-MM-DD
> tags:
>   - journal-club
>   - mwbr # ou engcomp
> ---
>
> > [!note] Em resumo
> > Uma frase resumindo do que o artigo trata.
>
> _Autores completos (Ano)_
>
> ## Resumo
> Síntese curta do artigo — problema, método, resultado principal.
>
> ## Discussão
> O que o grupo discutiu de fato: pontos levantados, críticas, dúvidas, conexões com outros artigos/projetos.
>
> [Ver no arXiv](https://arxiv.org/abs/XXXX.XXXXX)
> ```

---

## 🔗 Referências e correlatos

- [Pesquisa — visão geral](pt-br/research)
