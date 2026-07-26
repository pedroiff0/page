# Site pessoal — Pedro Henrique

Site acadêmico/pessoal, multilíngue (PT-BR completo; EN parcial; ES/FR só a página inicial), publicado via GitHub Pages a cada push em `main`:

🔗 **https://pedroiff0.github.io/page/** (migrando para **www.phrandrade.com**, ver `baseUrl` em `quartz.config.yaml`)

Construído com [Quartz](https://quartz.jzhao.xyz/), que transforma notas em Markdown num site estático navegável. O conteúdo é o próprio vault do Obsidian (pasta `content/`), editado diretamente pelo Pedro.

## Estrutura

```
content/
├── pt-br/         # conteúdo em português — idioma principal, sempre completo primeiro
├── en/            # conteúdo em inglês — tradução parcial
├── es/, fr/       # só a página inicial, com aviso de tradução em preparação
├── templates/     # templates do QuickAdd (Blog, Projeto, Pesquisa, Aula, Evento, Protegido...)
└── assets/        # imagens e outros arquivos estáticos, compartilhados entre os idiomas
quartz/            # motor do Quartz (fork de jackyzha0/quartz), componentes e estilos customizados
local-plugins/     # plugins próprios do fork, commitados no repo (photo-carousel, page-title-i18n)
scripts/           # utilitários de manutenção (ex: sync-material.sh)
```

Seções do site (dentro de cada idioma): Pesquisa, Recursos (incluindo Computação, Curso ON e notas de eventos como a Escola de Inverno), Mídia (participações em feiras e congressos, por ano), Projetos, Blog.

**Convenção importante**: os slugs de pasta/arquivo são idênticos entre idiomas (`en/research/x` ↔ `pt-br/research/x`) — é isso que faz o botão de trocar idioma funcionar sem mapear cada página manualmente. Detalhes de convenções e decisões de arquitetura estão em [`CLAUDE.md`](./CLAUDE.md) e [`content/CLAUDE.md`](./content/CLAUDE.md).

## Rodando localmente

```bash
npm install
npx quartz plugin install   # instala os plugins da comunidade usados no site
npx quartz build --serve    # http://localhost:8080, recarrega sozinho a cada save
```

## Qualidade

```bash
npm run check   # tsc --noEmit + prettier --check
npm run format   # prettier --write
npm test         # roda os testes sob quartz/
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
