# quartz-site

Site pessoal/acadêmico do Pedro Henrique, publicado em https://pedroiff0.github.io/page/ via GitHub Actions a cada push em `main`.

## Estrutura de conteúdo

- `content/en/...` e `content/pt-br/...` — conteúdo bilíngue. **Os slugs (pastas e arquivos) são idênticos nos dois idiomas** — só o segmento de idioma muda (`en/research/x` ↔ `pt-br/research/x`). Isso é o que permite o toggle de idioma (`quartz/components/LanguageToggle.tsx`) funcionar sem um dicionário de tradução por pasta. Ao criar conteúdo novo, sempre espelhar o nome da pasta/arquivo nos dois idiomas, mesmo que o conteúdo interno ainda não exista em um deles.
- Todo `index.md` de seção (research, resource, classes, media, publications, blog) precisa de `order: N` no frontmatter — controla a ordem no Explorer (barra lateral). Ferramentas de sync (Quartz Syncer, `npx quartz sync`) às vezes derrubam esse campo ao normalizar frontmatter — conferir depois de qualquer sync.
- Links internos devem usar o **caminho completo a partir da raiz do conteúdo** (ex: `pt-br/research/anomaly-detection`), nunca `./relativo`. A estratégia `markdownLinkResolution: shortest` do Quartz não usa a quantidade de `.` pra calcular profundidade — ela ignora os pontos e tenta casar o restante com um slug existente. `./foo` só funciona se existir um arquivo `foo.md` na raiz.

## Vault Obsidian

Este diretório (`content/`) é o vault Obsidian de verdade (`.obsidian/` na raiz de `content/`) — não é uma cópia. Publicação normalmente acontece via:

1. **Quartz Syncer** (plugin do Obsidian) — publica notas marcadas com `publish: true`. Tem um bug conhecido e aberto onde a central de publicação mostra "sucesso" mas não empurra nada de fato ([issue #123](https://github.com/saberzero1/quartz-syncer/issues/123)). Se isso acontecer, publicar manualmente com `npx quartz sync`.
2. **`npx quartz sync`** — puxa, commita e dá push. Confiável, usar como plano B.

**Cuidado**: publicações via Quartz Syncer refletem o estado local do vault Obsidian no momento do clique. Se este ambiente (onde outra sessão/Claude está editando) fez mudanças que ainda não "apareceram" no Obsidian local (ex: arquivos criados diretamente aqui), uma sincronização do plugin pode tentar reverter/apagar esse conteúdo. Sempre `git fetch && git log origin/main` antes de assumir que o remoto está no estado esperado, e resolver conflitos preservando conteúdo novo em vez de aceitar cegamente o lado remoto.

## Material de `hardcore-life` (outro vault)

`/home/pedro/Documentos/hardcore-life` é um vault Obsidian separado (notas pessoais, projetos, recursos de estudo). **Não é a fonte do site** — é de onde materiais específicos são selecionados e copiados manualmente, um de cada vez, nunca em bloco.

- Use `scripts/sync-material.sh "<caminho dentro de hardcore-life>" <topic-slug>` pra copiar um arquivo pra `content/assets/computacao/<slug>/`. O script avisa (mas não bloqueia) se o nome do arquivo bate com padrões suspeitos (nome completo do usuário, "prova", "avaliação", fontes pirata como z-lib/kupdf/pdfcoffee).
- **Nunca espelhar `05 - Recursos` inteiro.** Boa parte do conteúdo lá é: (a) cópias de livros com direitos autorais de terceiros, ou (b) provas/trabalhos pessoais com nome completo. Publicar isso no site público seria infração de copyright e exposição de dados pessoais, respectivamente.
- Artigos científicos (`01 - Projetos/Anomaly_Detection/papers/`): a pasta `Anotacoes/` tem sínteses em PT geradas automaticamente (pdftotext/OCR) — algumas têm erro de extração visível (símbolos gregos, fórmulas quebradas). Ao publicar, extrair só a seção `## Síntese PT (didática)` (geralmente limpa) e a citação/BibTeX de `Notes/`; **não publicar os blocos de citação direta/OCR bruto**.

## Deploy

Workflow em `.github/workflows/deploy-gh-pages.yaml`. Passos importantes que não são óbvios:

- `npx quartz plugin install` tem que rodar **antes** do build — o script `npm run install-plugins` do `package.json` está quebrado (erro de import de `.scss` fora de bundler), não usar.
- `npm ci` exige `package-lock.json` sincronizado — se o build falhar em "Install Dependencies", rodar `npm install` local e commitar o lockfile atualizado.
