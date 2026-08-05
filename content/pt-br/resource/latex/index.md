---
publish: true
title: "LaTeX & Escrita Acadêmica"
created: '2026-08-04'
modified: '2026-08-04'
tags:
  - latex
  - escrita-academica
  - abnt
  - ifftese
  - relatex
---

# LaTeX & Escrita Acadêmica

Bem-vindo ao repositório oficial da formação em **LaTeX & Escrita Acadêmica** do **Instituto Federal Fluminense (IFF) — Campus Bom Jesus do Itabapoana**, ministrada pelo **Prof. Dr. Pedro Henrique Rocha de Andrade**.

Esta plataforma centraliza o referencial teórico-metodológico e a arquitetura de automação documental **ReLaTeX**, promovendo o alinhamento integral entre rigor científico (**ABNT NBR 14724, NBR 10520, NBR 6023, NBR 6027, NBR 6028 e IBGE 1993**) e excelência tipográfica.

---

## 📚 Material Suplementar e Documentos Oficiais

Os documentos institucionais abaixo contêm a programação integral de 80 horas (20 Aulas de 4 tempos de 50 minutos), critérios de avaliação, código de ética científica e diretrizes de uso transparente de Inteligência Artificial:

- **[📅 Planejamento Letivo e Cronograma de Atividades](/pt-br/resource/latex/planejamento-e-cronograma)**  
  *Planejamento analítico das 20 aulas, divisão em 5 módulos didáticos, matriz de competências e referencial normativo ABNT.*
- **[📜 Código de Conduta, Ética na Pesquisa e Diretrizes Acadêmicas](/pt-br/resource/latex/codigo-de-conduta-e-diretrizes)**  
  *Código de ética científica, política institucional de integridade contra plágio/autoplágio, regimento de uso de IA (LLMs) e boas práticas de laboratório.*
- **[🏛️ Guia Oficial de Modelos, Classes e Pacotes ReLaTeX](/pt-br/resource/latex/modelos-de-documento)**  
  *Referência técnica unificada com documentação canônica das classes `ifftese.cls`, `iffposter.cls`, `relatoriocorp.cls` e pacotes `metadados.sty` e `macros.sty`.*

---

## 📊 Forma de Avaliação (Em Dois Bimestres) e Cronograma Letivo

> **📅 Período Letivo:** **24/08/2026 a 20/12/2026**  
> **⏰ Horário dos Encontros:** **Toda Terça-feira, das 14h30 às 17h30** (4 tempos de 50 minutos / aula teórica e laboratório prático)  
> **👨‍🏫 Professor Responsável:** **Prof. Dr. Pedro Henrique Rocha de Andrade**  

A avaliação da disciplina ocorre de forma formativa e somativa, estruturada em dois bimestres temáticos com focos avaliativos distintos. **Os pesos e datas apresentados são flexíveis**, podendo ser adaptados pelo professor conforme o andamento da turma em laboratório:

- **🔹 1º Bimestre — Metodologia Científica, Normalização e ABNT (Aulas 01 a 10):**
  - **60% — Trabalho Prático de Escrita Acadêmica:** Elaboração fundamentada de elementos pré-textuais, introdução com explicitação de lacuna de pesquisa (*Research Gap*), revisão sistemática da literatura (PRISMA 2020) e metodologia científica em conformidade com as normas ABNT vigentes.
  - **40% — Teste Prático em Sala:** Avaliação prática contínua em laboratório durante os encontros do primeiro bimestre (exercícios de normalização, citações ABNT NBR 10520:2023, referências NBR 6023 e tabelas IBGE 1993).

- **🔹 2º Bimestre — Engenharia TeX, Customização e Automação ReLaTeX (Aulas 11 a 20):**
  - **80% — Implementação Customizada e Diferenciada em LaTeX:** Desenvolvimento de um projeto acadêmico original ou monografia partindo da **base do modelo institucional do professor** (`ifftese.cls` e `slidesiffmodelo.cls`), implementando modificações e melhorias próprias, macros customizadas (`macros.sty`), tabelas `booktabs` e gráficos vetoriais `TikZ`/`PGFPlots`.
  - **20% — Teste Prático em Sala:** Avaliação prática em laboratório com resolução de erros de compilação, gestão bibliográfica com Biber e versionamento Git limpo.

---

## 🎨 Carrossel de Aulas (Acesso Rápido)

Acesse diretamente as notas de aula ilustradas pelas capas autênticas dos slides institucionais de cada encontro:

<!-- COURSE_CAROUSEL_START -->
<style>
.course-carousel-wrapper {
  display: flex;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  gap: 1.5rem;
  padding: 1.5rem 0.5rem;
  scrollbar-width: thin;
  scrollbar-color: var(--secondary, #0077b6) transparent;
  -webkit-overflow-scrolling: touch;
}
.course-carousel-card {
  flex: 0 0 280px;
  scroll-snap-align: start;
  border: 1px solid var(--lightgray, #e2e8f0);
  border-radius: 14px;
  overflow: hidden;
  background: var(--light, #ffffff);
  box-shadow: 0 4px 15px rgba(0,0,0,0.06);
  transition: all 0.35s cubic-bezier(0.25, 0.8, 0.25, 1);
  display: flex;
  flex-direction: column;
  text-decoration: none;
  position: relative;
}
.course-carousel-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 14px 28px rgba(0,0,0,0.14);
  border-color: var(--secondary, #0077b6);
}
.course-carousel-thumb-box {
  position: relative;
  width: 100%;
  height: 160px;
  overflow: hidden;
  background: #1e293b;
}
.course-carousel-thumb {
  width: 100%;
  height: 100%;
  object-fit: cover;
  filter: blur(3.5px) brightness(0.85);
  transform: scale(1.08);
  transition: filter 0.4s ease, transform 0.4s ease, brightness 0.4s ease;
}
.course-carousel-card:hover .course-carousel-thumb {
  filter: blur(0px) brightness(1);
  transform: scale(1.0);
}
.course-carousel-badge {
  position: absolute;
  top: 12px;
  left: 12px;
  background: rgba(0, 0, 0, 0.75);
  color: #fff;
  padding: 4px 10px;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 700;
  backdrop-filter: blur(4px);
  border: 1px solid rgba(255,255,255,0.2);
  z-index: 2;
}
.course-carousel-body {
  padding: 1.25rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  flex-grow: 1;
}
.course-carousel-title {
  font-size: 0.98rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  color: var(--dark, #0f172a);
  line-height: 1.35;
}
.course-carousel-desc {
  font-size: 0.82rem;
  color: var(--gray, #64748b);
  line-height: 1.45;
  margin: 0;
}
</style>

<div class="course-carousel-wrapper">
  <a href="/pt-br/resource/latex/aula-01-epistemologia-problematizacao-e-hipoteses" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 01</span>
      <img src="/assets/biblioteca/latex-escrita/thumbs/aula-01.png" alt="Capa Aula 01" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Epistemologia, Problematização e Hipóteses</div>
      <p class="course-carousel-desc">Normas em Foco: CEP/CONEP</p>
    </div>
  </a>
  <a href="/pt-br/resource/latex/aula-02-objetivos-taxonomia-de-bloom-e-justificativa" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 02</span>
      <img src="/assets/biblioteca/latex-escrita/thumbs/aula-02.png" alt="Capa Aula 02" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Objetivos, Taxonomia de Bloom e Justificativa</div>
      <p class="course-carousel-desc">Normas em Foco: ABNT NBR 14724 / CEP/CONEP</p>
    </div>
  </a>
  <a href="/pt-br/resource/latex/aula-03-resumo-abstract-e-palavras-chave-nbr-6028" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 03</span>
      <img src="/assets/biblioteca/latex-escrita/thumbs/aula-03.png" alt="Capa Aula 03" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Resumo, Abstract e Palavras-Chave (NBR 6028:2021)</div>
      <p class="course-carousel-desc">Normas em Foco: ABNT NBR 6028 / ABNT NBR 6028:2021</p>
    </div>
  </a>
  <a href="/pt-br/resource/latex/aula-04-elementos-pre-textuais-nbr-14724" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 04</span>
      <img src="/assets/biblioteca/latex-escrita/thumbs/aula-04.png" alt="Capa Aula 04" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Elementos Pré-Textuais NBR 14724</div>
      <p class="course-carousel-desc">Normas em Foco: ABNT NBR 14724 / ABNT NBR 6027:2012</p>
    </div>
  </a>
  <a href="/pt-br/resource/latex/aula-05-introducao-contextualizacao-e-lacuna-de-pesquisa" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 05</span>
      <img src="/assets/biblioteca/latex-escrita/thumbs/aula-05.png" alt="Capa Aula 05" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Introdução e Lacuna de Pesquisa (*Research Gap*)</div>
      <p class="course-carousel-desc">Normas em Foco: ABNT NBR 14724 / CEP/CONEP</p>
    </div>
  </a>
  <a href="/pt-br/resource/latex/aula-06-revisao-sistematica-da-literatura-e-protocolo-prisma" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 06</span>
      <img src="/assets/biblioteca/latex-escrita/thumbs/aula-06.png" alt="Capa Aula 06" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Revisão Sistemática da Literatura e Protocolo PRISMA 2020</div>
      <p class="course-carousel-desc">Normas em Foco: ABNT NBR 14724 / ABNT NBR 6023:2018</p>
    </div>
  </a>
  <a href="/pt-br/resource/latex/aula-07-metodologia-materiais-e-reprodutibilidade" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 07</span>
      <img src="/assets/biblioteca/latex-escrita/thumbs/aula-07.png" alt="Capa Aula 07" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Metodologia, Materiais e Reprodutibilidade na ABNT</div>
      <p class="course-carousel-desc">Normas em Foco: ABNT NBR 14724:2011 / ABNT NBR 6023:2018</p>
    </div>
  </a>
  <a href="/pt-br/resource/latex/aula-08-etica-plataforma-brasil-e-uso-de-ia" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 08</span>
      <img src="/assets/biblioteca/latex-escrita/thumbs/aula-08.png" alt="Capa Aula 08" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Ética na Pesquisa (Plataforma Brasil) e IA</div>
      <p class="course-carousel-desc">Normas em Foco: ABNT NBR 6023:2018 / CEP/CONEP</p>
    </div>
  </a>
  <a href="/pt-br/resource/latex/aula-09-resultados-tabelas-ibge-vs-quadros-abnt" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 09</span>
      <img src="/assets/biblioteca/latex-escrita/thumbs/aula-09.png" alt="Capa Aula 09" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Resultados: Tabelas IBGE vs. Quadros ABNT</div>
      <p class="course-carousel-desc">Normas em Foco: ABNT NBR 14724 / CEP/CONEP</p>
    </div>
  </a>
  <a href="/pt-br/resource/latex/aula-10-discussao-citacoes-nbr-10520-e-referencias-nbr-6023" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 10</span>
      <img src="/assets/biblioteca/latex-escrita/thumbs/aula-10.png" alt="Capa Aula 10" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Discussão, Citações (10520) e Referências (6023)</div>
      <p class="course-carousel-desc">Normas em Foco: ABNT NBR 10520:2023 / ABNT NBR 6023</p>
    </div>
  </a>
  <a href="/pt-br/resource/latex/aula-11-arquitetura-latex-motores-tex-e-preambulo-tex" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 11</span>
      <img src="/assets/biblioteca/latex-escrita/thumbs/aula-11.png" alt="Capa Aula 11" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Arquitetura do Kernel LaTeX2e, Motores PDFLaTeX/LuaLaTeX/XeLaTeX e Estrutura do Preâmbulo .tex</div>
      <p class="course-carousel-desc">Normas em Foco: CEP/CONEP</p>
    </div>
  </a>
  <a href="/pt-br/resource/latex/aula-12-sintaxe-matematica-amsmath-e-tabelas-booktabs" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 12</span>
      <img src="/assets/biblioteca/latex-escrita/thumbs/aula-12.png" alt="Capa Aula 12" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Sintaxe Canônica, Ambientes Matemáticos Avançados (amsmath) e Tabelas (booktabs)</div>
      <p class="course-carousel-desc">Normas em Foco: CEP/CONEP</p>
    </div>
  </a>
  <a href="/pt-br/resource/latex/aula-13-modularizacao-multi-arquivo-e-biblatex-biber" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 13</span>
      <img src="/assets/biblioteca/latex-escrita/thumbs/aula-13.png" alt="Capa Aula 13" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Modularização Multi-arquivo e Gestão Bibliográfica com biblatex-biber</div>
      <p class="course-carousel-desc">Normas em Foco: CEP/CONEP</p>
    </div>
  </a>
  <a href="/pt-br/resource/latex/aula-14-graficos-vetoriais-tikz-e-pgfplots" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 14</span>
      <img src="/assets/biblioteca/latex-escrita/thumbs/aula-14.png" alt="Capa Aula 14" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Computação Gráfica Vetorial Programável com TikZ e Gráficos PGFPlots</div>
      <p class="course-carousel-desc">Normas em Foco: CEP/CONEP</p>
    </div>
  </a>
  <a href="/pt-br/resource/latex/aula-15-engenharia-do-arquivo-de-metadados-sty" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 15</span>
      <img src="/assets/biblioteca/latex-escrita/thumbs/aula-15.png" alt="Capa Aula 15" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Engenharia de Metadados: Estrutura de metadados.sty, Escopo e Flexão de Gênero</div>
      <p class="course-carousel-desc">Normas em Foco: CEP/CONEP</p>
    </div>
  </a>
  <a href="/pt-br/resource/latex/aula-16-desenvolvimento-de-pacotes-e-macros-sty" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 16</span>
      <img src="/assets/biblioteca/latex-escrita/thumbs/aula-16.png" alt="Capa Aula 16" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Desenvolvimento de Pacotes .sty - Programação TeX e Macros</div>
      <p class="course-carousel-desc">Normas em Foco: CEP/CONEP</p>
    </div>
  </a>
  <a href="/pt-br/resource/latex/aula-17-engenharia-da-classe-ifftese-cls" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 17</span>
      <img src="/assets/biblioteca/latex-escrita/thumbs/aula-17.png" alt="Capa Aula 17" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Engenharia de Classes .cls - Anatomia da ifftese e abntex2</div>
      <p class="course-carousel-desc">Normas em Foco: ABNT NBR 14724 / CEP/CONEP</p>
    </div>
  </a>
  <a href="/pt-br/resource/latex/aula-18-customizacao-de-floats-fancyhdr-e-nbr-6027" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 18</span>
      <img src="/assets/biblioteca/latex-escrita/thumbs/aula-18.png" alt="Capa Aula 18" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Controle Avançado de Floats e NBR 6027</div>
      <p class="course-carousel-desc">Normas em Foco: CEP/CONEP</p>
    </div>
  </a>
  <a href="/pt-br/resource/latex/aula-19-classes-especializadas-if-beamer-iffposter-relatoriocorp" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 19</span>
      <img src="/assets/biblioteca/latex-escrita/thumbs/aula-19.png" alt="Capa Aula 19" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Classes Especializadas (Beamer, Poster e Relatório)</div>
      <p class="course-carousel-desc">Normas em Foco: CEP/CONEP</p>
    </div>
  </a>
  <a href="/pt-br/resource/latex/aula-20-automacao-latexmkrc-git-e-integracao-continua" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 20</span>
      <img src="/assets/biblioteca/latex-escrita/thumbs/aula-20.png" alt="Capa Aula 20" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Automação LaTeX, Git e Integração Contínua CI/CD</div>
      <p class="course-carousel-desc">Normas em Foco: CEP/CONEP</p>
    </div>
  </a>
</div>
<!-- COURSE_CAROUSEL_END -->

---

## 📅 Ementa Analítica por Módulos

A programação do curso está estruturada em **5 Módulos Didáticos**, cada um composto por 4 encontros intensivos (4 tempos de 50 minutos / 3h20). Para cada aula, o estudante dispõe de **Notas de Aula** completas em português e dos **Slides de Apresentação** nos formatos LaTeX Institucional (`if-beamer.cls`) e PowerPoint Widescreen (`.pptx` / 16:9).

<!-- COURSE_TABLE_START -->
### 📘 Módulo I — Epistemologia, Metodologia Científica e Elementos Pré-Textuais (Aulas 01 a 04)

- **Aula 01: [Epistemologia, Problematização e Hipóteses](/pt-br/resource/latex/aula-01-epistemologia-problematizacao-e-hipoteses)**  
  *Escopo e Normas:* CEP/CONEP  
  *Material Didático:* [📄 LaTeX Branco](/assets/biblioteca/latex-escrita/slides-latex/aula-01-branco.pdf) • [📄 LaTeX Preto](/assets/biblioteca/latex-escrita/slides-latex/aula-01-preto.pdf) • [📝 Notas Institucionais](/assets/biblioteca/latex-escrita/notes-latex/aula-01.pdf) • [🛠️ Recursos Adicionais](/pt-br/resource/latex/aula-01-epistemologia-problematizacao-e-hipoteses#recursos-adicionais)  

- **Aula 02: [Objetivos, Taxonomia de Bloom e Justificativa](/pt-br/resource/latex/aula-02-objetivos-taxonomia-de-bloom-e-justificativa)**  
  *Escopo e Normas:* ABNT NBR 14724 / CEP/CONEP  
  *Material Didático:* [📄 LaTeX Branco](/assets/biblioteca/latex-escrita/slides-latex/aula-02-branco.pdf) • [📄 LaTeX Preto](/assets/biblioteca/latex-escrita/slides-latex/aula-02-preto.pdf) • [📝 Notas Institucionais](/assets/biblioteca/latex-escrita/notes-latex/aula-02.pdf) • [🛠️ Recursos Adicionais](/pt-br/resource/latex/aula-02-objetivos-taxonomia-de-bloom-e-justificativa#recursos-adicionais)  

- **Aula 03: [Resumo, Abstract e Palavras-Chave (NBR 6028:2021)](/pt-br/resource/latex/aula-03-resumo-abstract-e-palavras-chave-nbr-6028)**  
  *Escopo e Normas:* ABNT NBR 6028 / ABNT NBR 6028:2021  
  *Material Didático:* [📄 LaTeX Branco](/assets/biblioteca/latex-escrita/slides-latex/aula-03-branco.pdf) • [📄 LaTeX Preto](/assets/biblioteca/latex-escrita/slides-latex/aula-03-preto.pdf) • [📝 Notas Institucionais](/assets/biblioteca/latex-escrita/notes-latex/aula-03.pdf) • [🛠️ Recursos Adicionais](/pt-br/resource/latex/aula-03-resumo-abstract-e-palavras-chave-nbr-6028#recursos-adicionais)  

- **Aula 04: [Elementos Pré-Textuais NBR 14724](/pt-br/resource/latex/aula-04-elementos-pre-textuais-nbr-14724)**  
  *Escopo e Normas:* ABNT NBR 14724 / ABNT NBR 6027:2012  
  *Material Didático:* [📄 LaTeX Branco](/assets/biblioteca/latex-escrita/slides-latex/aula-04-branco.pdf) • [📄 LaTeX Preto](/assets/biblioteca/latex-escrita/slides-latex/aula-04-preto.pdf) • [📝 Notas Institucionais](/assets/biblioteca/latex-escrita/notes-latex/aula-04.pdf) • [🛠️ Recursos Adicionais](/pt-br/resource/latex/aula-04-elementos-pre-textuais-nbr-14724#recursos-adicionais)  

---

### 📘 Módulo II — Estrutura Textual, Introdução, PRISMA e Metodologia (Aulas 05 a 08)

- **Aula 05: [Introdução e Lacuna de Pesquisa (*Research Gap*)](/pt-br/resource/latex/aula-05-introducao-contextualizacao-e-lacuna-de-pesquisa)**  
  *Escopo e Normas:* ABNT NBR 14724 / CEP/CONEP  
  *Material Didático:* [📄 LaTeX Branco](/assets/biblioteca/latex-escrita/slides-latex/aula-05-branco.pdf) • [📄 LaTeX Preto](/assets/biblioteca/latex-escrita/slides-latex/aula-05-preto.pdf) • [📝 Notas Institucionais](/assets/biblioteca/latex-escrita/notes-latex/aula-05.pdf) • [🛠️ Recursos Adicionais](/pt-br/resource/latex/aula-05-introducao-contextualizacao-e-lacuna-de-pesquisa#recursos-adicionais)  

- **Aula 06: [Revisão Sistemática da Literatura e Protocolo PRISMA 2020](/pt-br/resource/latex/aula-06-revisao-sistematica-da-literatura-e-protocolo-prisma)**  
  *Escopo e Normas:* ABNT NBR 14724 / ABNT NBR 6023:2018  
  *Material Didático:* [📄 LaTeX Branco](/assets/biblioteca/latex-escrita/slides-latex/aula-06-branco.pdf) • [📄 LaTeX Preto](/assets/biblioteca/latex-escrita/slides-latex/aula-06-preto.pdf) • [📝 Notas Institucionais](/assets/biblioteca/latex-escrita/notes-latex/aula-06.pdf) • [🛠️ Recursos Adicionais](/pt-br/resource/latex/aula-06-revisao-sistematica-da-literatura-e-protocolo-prisma#recursos-adicionais)  

- **Aula 07: [Metodologia, Materiais e Reprodutibilidade na ABNT](/pt-br/resource/latex/aula-07-metodologia-materiais-e-reprodutibilidade)**  
  *Escopo e Normas:* ABNT NBR 14724:2011 / ABNT NBR 6023:2018  
  *Material Didático:* [📄 LaTeX Branco](/assets/biblioteca/latex-escrita/slides-latex/aula-07-branco.pdf) • [📄 LaTeX Preto](/assets/biblioteca/latex-escrita/slides-latex/aula-07-preto.pdf) • [📝 Notas Institucionais](/assets/biblioteca/latex-escrita/notes-latex/aula-07.pdf) • [🛠️ Recursos Adicionais](/pt-br/resource/latex/aula-07-metodologia-materiais-e-reprodutibilidade#recursos-adicionais)  

- **Aula 08: [Ética na Pesquisa (Plataforma Brasil) e IA](/pt-br/resource/latex/aula-08-etica-plataforma-brasil-e-uso-de-ia)**  
  *Escopo e Normas:* ABNT NBR 6023:2018 / CEP/CONEP  
  *Material Didático:* [📄 LaTeX Branco](/assets/biblioteca/latex-escrita/slides-latex/aula-08-branco.pdf) • [📄 LaTeX Preto](/assets/biblioteca/latex-escrita/slides-latex/aula-08-preto.pdf) • [📝 Notas Institucionais](/assets/biblioteca/latex-escrita/notes-latex/aula-08.pdf) • [🛠️ Recursos Adicionais](/pt-br/resource/latex/aula-08-etica-plataforma-brasil-e-uso-de-ia#recursos-adicionais)  

---

### 📘 Módulo III — Resultados, Discussão, Citações NBR 10520 e Referências NBR 6023 (Aulas 09 a 12)

- **Aula 09: [Resultados: Tabelas IBGE vs. Quadros ABNT](/pt-br/resource/latex/aula-09-resultados-tabelas-ibge-vs-quadros-abnt)**  
  *Escopo e Normas:* ABNT NBR 14724 / CEP/CONEP  
  *Material Didático:* [📄 LaTeX Branco](/assets/biblioteca/latex-escrita/slides-latex/aula-09-branco.pdf) • [📄 LaTeX Preto](/assets/biblioteca/latex-escrita/slides-latex/aula-09-preto.pdf) • [📝 Notas Institucionais](/assets/biblioteca/latex-escrita/notes-latex/aula-09.pdf) • [🛠️ Recursos Adicionais](/pt-br/resource/latex/aula-09-resultados-tabelas-ibge-vs-quadros-abnt#recursos-adicionais)  

- **Aula 10: [Discussão, Citações (10520) e Referências (6023)](/pt-br/resource/latex/aula-10-discussao-citacoes-nbr-10520-e-referencias-nbr-6023)**  
  *Escopo e Normas:* ABNT NBR 10520:2023 / ABNT NBR 6023  
  *Material Didático:* [📄 LaTeX Branco](/assets/biblioteca/latex-escrita/slides-latex/aula-10-branco.pdf) • [📄 LaTeX Preto](/assets/biblioteca/latex-escrita/slides-latex/aula-10-preto.pdf) • [📝 Notas Institucionais](/assets/biblioteca/latex-escrita/notes-latex/aula-10.pdf) • [🛠️ Recursos Adicionais](/pt-br/resource/latex/aula-10-discussao-citacoes-nbr-10520-e-referencias-nbr-6023#recursos-adicionais)  

- **Aula 11: [Arquitetura do Kernel LaTeX2e, Motores PDFLaTeX/LuaLaTeX/XeLaTeX e Estrutura do Preâmbulo .tex](/pt-br/resource/latex/aula-11-arquitetura-latex-motores-tex-e-preambulo-tex)**  
  *Escopo e Normas:* CEP/CONEP  
  *Material Didático:* [📄 LaTeX Branco](/assets/biblioteca/latex-escrita/slides-latex/aula-11-branco.pdf) • [📄 LaTeX Preto](/assets/biblioteca/latex-escrita/slides-latex/aula-11-preto.pdf) • [📝 Notas Institucionais](/assets/biblioteca/latex-escrita/notes-latex/aula-11.pdf) • [🛠️ Recursos Adicionais](/pt-br/resource/latex/aula-11-arquitetura-latex-motores-tex-e-preambulo-tex#recursos-adicionais)  

- **Aula 12: [Sintaxe Canônica, Ambientes Matemáticos Avançados (amsmath) e Tabelas (booktabs)](/pt-br/resource/latex/aula-12-sintaxe-matematica-amsmath-e-tabelas-booktabs)**  
  *Escopo e Normas:* CEP/CONEP  
  *Material Didático:* [📄 LaTeX Branco](/assets/biblioteca/latex-escrita/slides-latex/aula-12-branco.pdf) • [📄 LaTeX Preto](/assets/biblioteca/latex-escrita/slides-latex/aula-12-preto.pdf) • [📝 Notas Institucionais](/assets/biblioteca/latex-escrita/notes-latex/aula-12.pdf) • [🛠️ Recursos Adicionais](/pt-br/resource/latex/aula-12-sintaxe-matematica-amsmath-e-tabelas-booktabs#recursos-adicionais)  

---

### 📗 Módulo IV — Arquitetura LaTeX (.tex), Motores, Sintaxe, Tabelas e Gráficos (Aulas 13 a 16)

- **Aula 13: [Modularização Multi-arquivo e Gestão Bibliográfica com biblatex-biber](/pt-br/resource/latex/aula-13-modularizacao-multi-arquivo-e-biblatex-biber)**  
  *Escopo e Normas:* CEP/CONEP  
  *Material Didático:* [📄 LaTeX Branco](/assets/biblioteca/latex-escrita/slides-latex/aula-13-branco.pdf) • [📄 LaTeX Preto](/assets/biblioteca/latex-escrita/slides-latex/aula-13-preto.pdf) • [📝 Notas Institucionais](/assets/biblioteca/latex-escrita/notes-latex/aula-13.pdf) • [🛠️ Recursos Adicionais](/pt-br/resource/latex/aula-13-modularizacao-multi-arquivo-e-biblatex-biber#recursos-adicionais)  

- **Aula 14: [Computação Gráfica Vetorial Programável com TikZ e Gráficos PGFPlots](/pt-br/resource/latex/aula-14-graficos-vetoriais-tikz-e-pgfplots)**  
  *Escopo e Normas:* CEP/CONEP  
  *Material Didático:* [📄 LaTeX Branco](/assets/biblioteca/latex-escrita/slides-latex/aula-14-branco.pdf) • [📄 LaTeX Preto](/assets/biblioteca/latex-escrita/slides-latex/aula-14-preto.pdf) • [📝 Notas Institucionais](/assets/biblioteca/latex-escrita/notes-latex/aula-14.pdf) • [🛠️ Recursos Adicionais](/pt-br/resource/latex/aula-14-graficos-vetoriais-tikz-e-pgfplots#recursos-adicionais)  

- **Aula 15: [Engenharia de Metadados: Estrutura de metadados.sty, Escopo e Flexão de Gênero](/pt-br/resource/latex/aula-15-engenharia-do-arquivo-de-metadados-sty)**  
  *Escopo e Normas:* CEP/CONEP  
  *Material Didático:* [📄 LaTeX Branco](/assets/biblioteca/latex-escrita/slides-latex/aula-15-branco.pdf) • [📄 LaTeX Preto](/assets/biblioteca/latex-escrita/slides-latex/aula-15-preto.pdf) • [📝 Notas Institucionais](/assets/biblioteca/latex-escrita/notes-latex/aula-15.pdf) • [🛠️ Recursos Adicionais](/pt-br/resource/latex/aula-15-engenharia-do-arquivo-de-metadados-sty#recursos-adicionais)  

- **Aula 16: [Desenvolvimento de Pacotes .sty - Programação TeX e Macros](/pt-br/resource/latex/aula-16-desenvolvimento-de-pacotes-e-macros-sty)**  
  *Escopo e Normas:* CEP/CONEP  
  *Material Didático:* [📄 LaTeX Branco](/assets/biblioteca/latex-escrita/slides-latex/aula-16-branco.pdf) • [📄 LaTeX Preto](/assets/biblioteca/latex-escrita/slides-latex/aula-16-preto.pdf) • [📝 Notas Institucionais](/assets/biblioteca/latex-escrita/notes-latex/aula-16.pdf) • [🛠️ Recursos Adicionais](/pt-br/resource/latex/aula-16-desenvolvimento-de-pacotes-e-macros-sty#recursos-adicionais)  

---

### 📗 Módulo V — Engenharia ReLaTeX (.cls e .sty), Metadados, Macros e Automação (Aulas 17 a 20)

- **Aula 17: [Engenharia de Classes .cls - Anatomia da ifftese e abntex2](/pt-br/resource/latex/aula-17-engenharia-da-classe-ifftese-cls)**  
  *Escopo e Normas:* ABNT NBR 14724 / CEP/CONEP  
  *Material Didático:* [📄 LaTeX Branco](/assets/biblioteca/latex-escrita/slides-latex/aula-17-branco.pdf) • [📄 LaTeX Preto](/assets/biblioteca/latex-escrita/slides-latex/aula-17-preto.pdf) • [📝 Notas Institucionais](/assets/biblioteca/latex-escrita/notes-latex/aula-17.pdf) • [🛠️ Recursos Adicionais](/pt-br/resource/latex/aula-17-engenharia-da-classe-ifftese-cls#recursos-adicionais)  

- **Aula 18: [Controle Avançado de Floats e NBR 6027](/pt-br/resource/latex/aula-18-customizacao-de-floats-fancyhdr-e-nbr-6027)**  
  *Escopo e Normas:* CEP/CONEP  
  *Material Didático:* [📄 LaTeX Branco](/assets/biblioteca/latex-escrita/slides-latex/aula-18-branco.pdf) • [📄 LaTeX Preto](/assets/biblioteca/latex-escrita/slides-latex/aula-18-preto.pdf) • [📝 Notas Institucionais](/assets/biblioteca/latex-escrita/notes-latex/aula-18.pdf) • [🛠️ Recursos Adicionais](/pt-br/resource/latex/aula-18-customizacao-de-floats-fancyhdr-e-nbr-6027#recursos-adicionais)  

- **Aula 19: [Classes Especializadas (Beamer, Poster e Relatório)](/pt-br/resource/latex/aula-19-classes-especializadas-if-beamer-iffposter-relatoriocorp)**  
  *Escopo e Normas:* CEP/CONEP  
  *Material Didático:* [📄 LaTeX Branco](/assets/biblioteca/latex-escrita/slides-latex/aula-19-branco.pdf) • [📄 LaTeX Preto](/assets/biblioteca/latex-escrita/slides-latex/aula-19-preto.pdf) • [📝 Notas Institucionais](/assets/biblioteca/latex-escrita/notes-latex/aula-19.pdf) • [🛠️ Recursos Adicionais](/pt-br/resource/latex/aula-19-classes-especializadas-if-beamer-iffposter-relatoriocorp#recursos-adicionais)  

- **Aula 20: [Automação LaTeX, Git e Integração Contínua CI/CD](/pt-br/resource/latex/aula-20-automacao-latexmkrc-git-e-integracao-continua)**  
  *Escopo e Normas:* CEP/CONEP  
  *Material Didático:* [📄 LaTeX Branco](/assets/biblioteca/latex-escrita/slides-latex/aula-20-branco.pdf) • [📄 LaTeX Preto](/assets/biblioteca/latex-escrita/slides-latex/aula-20-preto.pdf) • [📝 Notas Institucionais](/assets/biblioteca/latex-escrita/notes-latex/aula-20.pdf) • [🛠️ Recursos Adicionais](/pt-br/resource/latex/aula-20-automacao-latexmkrc-git-e-integracao-continua#recursos-adicionais)  

---

<!-- COURSE_TABLE_END -->

## 🏛️ Pacotes e Classes do Ecossistema ReLaTeX

O desenvolvimento de monografias, TCCs, relatórios de estágio e dissertações no Instituto Federal Fluminense apoia-se na centralização documental do **ReLaTeX**. Consulte a [página oficial de modelos](pt-br/resource/latex/modelos-de-documento) para exemplos completos de código.

```mermaid
graph TD
    A[Preâmbulo / main.tex] --> B[ifftese.cls / Classe Canônica NBR 14724]
    A --> C[metadados.sty / Dados Acadêmicos]
    A --> D[macros.sty / Produtividade e Tabelas ABNT]
    A --> E[if-beamer.cls / Slides de Defesa]
    A --> F[iffposter.cls / Pôster Científico A0]
    B --> G[Compilador PDFLaTeX + Biber]
    C --> G
    D --> G
    G --> H[Documento Final em Conformidade ABNT/IBGE]
```

---

## 📚 Material de Referência, Interdisciplinaridade e Conteúdo Suplementar

Abaixo, disponibilizamos referências canônicas internas (integração com disciplinas e laboratórios do IFF) e externas (portais de normalização científica, bases de dados e repositórios mundiais TeX) para complementar os estudos letivos:

### 🏛️ Interdisciplinaridade e Disciplinas do IFF — Campus Bom Jesus do Itabapoana
- **[📐 Álgebra Linear e Geometria Analítica I](/pt-br/resource/Engenharia-de-Computacao/1-periodo/algebra-linear-e-geometria-analitica-i/)** — *Aplicação prática de ambientes matemáticos (`amsmath`, `mathtools`), matrizes e equações diferenciais em LaTeX.*
- **[🏛️ Guia Oficial de Modelos, Classes e Pacotes ReLaTeX](/pt-br/resource/latex/modelos-de-documento)** — *Repositório institucional de modelos para trabalhos de conclusão de curso (`ifftese.cls`), pôsteres A0 (`iffposter.cls`) e relatórios técnicos.*
- **[📅 Planejamento Letivo e Cronograma de Atividades](/pt-br/resource/latex/planejamento-e-cronograma)** — *Estruturação analítica das 80 horas de formação em 20 encontros temáticos.*
- **[📜 Código de Conduta, Ética na Pesquisa e Diretrizes Acadêmicas](/pt-br/resource/latex/codigo-de-conduta-e-diretrizes)** — *Normativo disciplinar e boas práticas em laboratório de computação.*

### 🌐 Referências Externas, Manuais TeX e Normalização Mundial
- **[ABNT — Associação Brasileira de Normas Técnicas](https://www.abnt.org.br/)** — *Portal oficial de consulta às normas ABNT NBR 14724 (Trabalhos Acadêmicos), NBR 10520 (Citações) e NBR 6023 (Referências).*
- **[CTAN (Comprehensive TeX Archive Network)](https://ctan.org/)** — *O repositório mundial canônico de pacotes, documentações e classes LaTeX2e e LaTeX3.*
- **[Overleaf Documentation & TeX Live Guide](https://www.overleaf.com/learn)** — *Guias interativos, documentação de pacotes e tutoriais da linguagem LaTeX para pesquisadores.*
- **[Plataforma Brasil & CEP/CONEP](https://plataformabrasil.saude.gov.br/)** — *Base nacional e unificada dos registros de pesquisas envolvendo seres humanos para submissão aos Comitês de Ética.*
- **[PRISMA Statement 2020](http://www.prisma-statement.org/)** — *Diretrizes internacionais e fluxogramas recomendados para revisões sistemáticas da literatura e meta-análises.*
- **[IBGE — Normas de Apresentação Tabular (1993)](https://biblioteca.ibge.gov.br/)** — *Manual técnico oficial para elaboração, padronização e estruturação de tabelas estatísticas brasileiras.*
