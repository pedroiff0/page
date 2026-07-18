# Site pessoal — Pedro Henrique

Site acadêmico/pessoal, bilíngue (PT-BR / EN), publicado em:

🔗 **https://pedroiff0.github.io/page/**

Construído com [Quartz](https://quartz.jzhao.xyz/), que transforma notas em Markdown num site estático navegável. O conteúdo é o próprio vault do Obsidian (pasta `content/`), publicado automaticamente no GitHub Pages a cada push em `main`.

## Estrutura

```
content/
├── en/            # conteúdo em inglês
├── pt-br/         # conteúdo em português — inclui seções só-PT (Disciplinas, Recursos/Computação)
└── assets/        # imagens e outros arquivos estáticos, compartilhados entre os dois idiomas
quartz/            # motor do Quartz (fork de jackyzha0/quartz), componentes e estilos customizados
scripts/           # utilitários de manutenção (ex: sync-material.sh)
```

Seções do site: Pesquisa (incluindo Artigos — anotações de leitura), Recursos (incluindo Computação — arquivo de estudo), Disciplinas (grade curricular completa de Engenharia de Computação, IFF), Mídia, Publicações, Blog.

**Convenção importante**: os slugs de pasta/arquivo são idênticos nos dois idiomas (`en/research/x` ↔ `pt-br/research/x`) — é isso que faz o botão de trocar idioma funcionar sem mapear cada página manualmente. Detalhes de convenções e decisões de arquitetura estão em [`CLAUDE.md`](./CLAUDE.md).

## Rodando localmente

```bash
npm install
npx quartz plugin install   # instala os plugins da comunidade usados no site
npx quartz build --serve    # http://localhost:8080, recarrega sozinho a cada save
```

## Publicando

Editando pelo Obsidian: marcar a nota com a propriedade `publish` e usar a central de publicação do plugin [Quartz Syncer](https://github.com/saberzero1/quartz-syncer).

Pelo terminal:

```bash
npx quartz sync -m "descrição da mudança"
```

Qualquer um dos dois só empurra o Markdown para o GitHub — o build e o deploy em si rodam automaticamente via GitHub Actions (`.github/workflows/deploy-gh-pages.yaml`) depois do push.

## Créditos

Motor do site: [Quartz](https://github.com/jackyzha0/quartz), de Jacky Zhao — MIT License. Este repositório é um fork com conteúdo e alguns componentes/estilos próprios.
