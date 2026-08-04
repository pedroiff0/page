---
publish: true
title: "Nome do Novo Curso"
created: '2026-08-04'
modified: '2026-08-04'
tags:
  - curso
  - iff
  - engenharia
---

# Nome do Novo Curso

Bem-vindo ao repositório oficial da formação em **Nome do Novo Curso** do **Instituto Federal Fluminense (IFF) — Campus Bom Jesus do Itabapoana**, ministrada pelo **Prof. Dr. Pedro Henrique Rocha de Andrade**.

Esta plataforma centraliza o referencial teórico-metodológico, material suplementar, slides institucionais e notas de aula práticas da disciplina.

---

## 📚 Material Suplementar e Documentos Oficiais

Os documentos institucionais abaixo contêm a programação letiva completa, ementa analítica, critérios de avaliação e diretrizes acadêmicas:

- **[📅 Planejamento Letivo e Cronograma de Atividades](/pt-br/resource/latex/planejamento-e-cronograma)**  
  *Planejamento letivo detalhado, carga horária total e cronograma das aulas.*
- **[📜 Código de Conduta, Ética na Pesquisa e Diretrizes Acadêmicas](/pt-br/resource/latex/codigo-de-conduta-e-diretrizes)**  
  *Código de ética acadêmica, diretrizes de apresentação e critérios de avaliação.*

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
  <a href="/templates/ModeloCurso/aula-01-introducao-exemplo" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 01</span>
      <img src="/assets/biblioteca/modelo-curso/thumbs/aula-01.png" alt="Capa Aula 01" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Introdução e Fundamentação Teórica</div>
      <p class="course-carousel-desc">Normas em Foco: ABNT NBR 10520:2023 / ABNT NBR 14724</p>
    </div>
  </a>
  <a href="/templates/ModeloCurso/aula-02-fundamentos-exemplo" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 02</span>
      <img src="/assets/biblioteca/modelo-curso/thumbs/aula-02.png" alt="Capa Aula 02" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Fundamentos Metodológicos e Prática</div>
      <p class="course-carousel-desc">Normas em Foco: ABNT NBR 10520 / ABNT NBR 10520:2023</p>
    </div>
  </a>
</div>
<!-- COURSE_CAROUSEL_END -->

---

## 📅 Ementa Analítica por Módulos

A programação do curso é alimentada **automaticamente** a partir das aulas (`aula-*.md`) cadastradas nesta pasta. Sempre que uma nova aula for adicionada, a tabela será preenchida sozinha ao compilar o site ou executar `npm run update-courses`.

*(Acesso Restrito Institucional — Arquivos PDF Protegidos por Senha)*

<!-- COURSE_TABLE_START -->
### 📘 Módulo I — Epistemologia, Metodologia Científica e Elementos Pré-Textuais (Aulas 01 a 04)

- **Aula 01: [Introdução e Fundamentação Teórica](/templates/ModeloCurso/aula-01-introducao-exemplo)**  
  *Escopo e Normas:* ABNT NBR 10520:2023 / ABNT NBR 14724  
  *Material Didático:* [📄 LaTeX Branco](/assets/biblioteca/modelo-curso/slides-latex/aula-01-branco.pdf) • [📄 LaTeX Preto](/assets/biblioteca/modelo-curso/slides-latex/aula-01-preto.pdf) • [📊 PPTX Branco](/assets/biblioteca/modelo-curso/slides-pptx/aula-01-branco.pptx) • [📊 PPTX Preto](/assets/biblioteca/modelo-curso/slides-pptx/aula-01-preto.pptx) • [📝 Notas Institucionais](/assets/biblioteca/modelo-curso/notes-latex/aula-01.pdf) • [🛠️ Recursos Adicionais](/templates/ModeloCurso/aula-01-introducao-exemplo#recursos-adicionais)  

- **Aula 02: [Fundamentos Metodológicos e Prática](/templates/ModeloCurso/aula-02-fundamentos-exemplo)**  
  *Escopo e Normas:* ABNT NBR 10520 / ABNT NBR 10520:2023  
  *Material Didático:* [📄 LaTeX Branco](/assets/biblioteca/modelo-curso/slides-latex/aula-02-branco.pdf) • [📄 LaTeX Preto](/assets/biblioteca/modelo-curso/slides-latex/aula-02-preto.pdf) • [📊 PPTX Branco](/assets/biblioteca/modelo-curso/slides-pptx/aula-02-branco.pptx) • [📊 PPTX Preto](/assets/biblioteca/modelo-curso/slides-pptx/aula-02-preto.pptx) • [📝 Notas Institucionais](/assets/biblioteca/modelo-curso/notes-latex/aula-02.pdf) • [🛠️ Recursos Adicionais](/templates/ModeloCurso/aula-02-fundamentos-exemplo#recursos-adicionais)  

---

<!-- COURSE_TABLE_END -->
