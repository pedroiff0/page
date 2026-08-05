\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{slidesiffmodelo}[2026/05/30 Modelo de Slides IFF - Padrão CONFICT]

% --- Opções da Classe ---
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{beamer}}
\ProcessOptions\relax
\LoadClass{beamer}

% --- Pacotes Essenciais ---
\RequirePackage[T1]{fontenc}
\RequirePackage[brazilian]{babel}
\RequirePackage{graphicx, xcolor, tabularx, booktabs, tcolorbox, etoolbox}
\RequirePackage{orcidlink} 
\RequirePackage{caption}
\RequirePackage[alf,abnt-etal-text=it,abnt-emphasize=bf,abnt-etal-list=4,abnt-etal-cite=4]{abntex2cite}

% --- DEFINIÇÕES DE JORNAIS DE ASTRONOMIA ---
\def\aj{AJ} \def\araa{ARA\&A} \def\apj{ApJ} \def\apjl{ApJ} \def\apjs{ApJS}
\def\apss{Ap\&SS} \def\aap{A\&A} \def\aapr{A\&A~Rev.} \def\aaps{A\&AS}
\def\mnras{MNRAS} \def\pasp{PASP} \def\pasj{PASJ} \def\pasa{PASA}
\def\qjras{QJRAS} \def\nat{Nature} \def\aplett{Astrophys.~Lett.}
\def\aas{AAS} \def\eprint{e--print}

% --- VARIÁVEIS ASTRONÔMICAS ---
\newcommand{\feh}{[Fe/H]}
\newcommand{\mgfe}{[Mg/Fe]}
\newcommand{\teff}{$T_{\text{eff}}$}
\newcommand{\logg}{$\log g$}
\newcommand{\estrela}{$\bigstar$s }
\newcommand{\email}{\href{mailto:pedroiff0@gmail.com}{pedroiff0@gmail.com}}

% --- 1. NEUTRALIZAÇÃO DE CORES (Preto/Branco) ---
\setbeamercolor{normal text}{fg=black,bg=white}
\setbeamercolor{structure}{fg=black}
\setbeamercolor{title}{fg=black}
\setbeamercolor{frametitle}{fg=black}
\setbeamercolor{item}{fg=black}
\setbeamercolor{caption}{fg=black}
\setbeamercolor{caption name}{fg=black}

% --- 2. CONFIGURAÇÕES CRÍTICAS DE MARGEM, LAYOUT E LISTAS ---
\setbeamertemplate{navigation symbols}{} 
\setbeamertemplate{frametitle continuation}{} 
\usefonttheme{professionalfonts}

\setbeamersize{text margin left=0.4cm, text margin right=0.4cm}

\setlength{\leftmargini}{1.1em}  
\setlength{\leftmarginii}{1.0em} 
\setlength{\leftmarginiii}{1.0em} 

\addtobeamertemplate{itemize/enumerate body begin}{\vspace*{-2pt}}{}
\addtobeamertemplate{itemize/enumerate body end}{\vspace*{-2pt}}{}
\addtobeamertemplate{itemize i}{\setlength{\itemsep}{2pt}\setlength{\topsep}{0pt}\setlength{\parsep}{0pt}}{}
\addtobeamertemplate{enumerate i}{\setlength{\itemsep}{2pt}\setlength{\topsep}{0pt}\setlength{\parsep}{0pt}}{}

\setbeamertemplate{caption}[numbered]
\captionsetup{font=scriptsize, labelfont=bf, justification=centering, singlelinecheck=false, position=top, skip=0pt}

% --- 3. CONFIGURAÇÃO DINÂMICA DE ARQUIVOS, LOGOS E TAMANHOS ---
\let\@bgimg\empty
\let\@headerimg\empty
\let\@footerimg\empty
\let\@logoEsq\empty \let\@logoMeio\empty \let\@logoDir\empty 

\newcommand{\@headerheight}{1.5cm}
\newcommand{\@footerheight}{0.65cm}

\newcommand{\setbackgroundimage}[1]{\def\@bgimg{#1}}
\newcommand{\setheaderimage}[1]{\def\@headerimg{#1}}
\newcommand{\setfooterimage}[1]{\def\@footerimg{#1}}
\newcommand{\setheaderheight}[1]{\def\@headerheight{#1}}
\newcommand{\setfooterheight}[1]{\def\@footerheight{#1}}

\newcommand{\logoEsq}[2][1cm]{\def\@logoEsq{\includegraphics[height=#1,keepaspectratio]{#2}}}
\newcommand{\logoMeio}[2][1cm]{\def\@logoMeio{\includegraphics[height=#1,keepaspectratio]{#2}}}
\newcommand{\logoDir}[2][1cm]{\def\@logoDir{\includegraphics[height=#1,keepaspectratio]{#2}}}

% --- 4. PARÂMETROS CUSTOMIZADOS [img] e [small] (Com herança Total de fonte) ---
\newif\if@imgframe \@imgframefalse
\newif\if@smallframe \@smallframefalse

\define@key{beamerframe}{img}[true]{\global\@imgframetrue}
\define@key{beamerframe}{small}[true]{\global\@smallframetrue}

\addtobeamertemplate{frame begin}{}{%
    \if@imgframe \global\@smallframetrue \fi % img sempre implica em texto pequeno
    \if@smallframe 
        \scriptsize 
        % Força a redução nas fontes do Beamer (Sumário e Bibliografia)
        \setbeamerfont{section in toc}{size=\scriptsize}
        \setbeamerfont{subsection in toc}{size=\scriptsize}
        \setbeamerfont{bibliography item}{size=\scriptsize}
        \setbeamerfont{bibliography entry author}{size=\scriptsize}
        \setbeamerfont{bibliography entry title}{size=\scriptsize}
        \setbeamerfont{bibliography entry location}{size=\scriptsize}
        \setbeamerfont{bibliography entry note}{size=\scriptsize}
    \fi
}
\addtobeamertemplate{frame end}{}{%
    \if@smallframe 
        \normalsize 
        \global\@smallframefalse 
        \global\@imgframefalse
    \fi
}

% --- 5. AMBIENTE AUTOMÁTICO DE TEXTO + IMAGEM (Com herança de fonte) ---
\newenvironment{textoimagem}{%
    \begin{columns}[T, onlytextwidth]
    \begin{column}{0.4\textwidth}
        \if@smallframe \scriptsize \fi
}{%
    \end{column}
    \end{columns}
}

\newcommand{\colunaimagem}{%
    \end{column}
    \begin{column}{0.58\textwidth}
        \vspace*{-0.6cm} 
        \if@smallframe \scriptsize \fi
}

% --- 6. BACKGROUND, CABEÇALHOS E RODAPÉ ---
\setbeamertemplate{background}{
    \ifx\@bgimg\empty\else\includegraphics[width=\paperwidth, height=\paperheight, keepaspectratio=false]{\@bgimg}\fi
}

\setbeamertemplate{headline}{
    \ifx\@headerimg\empty\else
        \begin{beamercolorbox}[wd=\paperwidth, ht=\@headerheight, dp=0cm]{}
            \includegraphics[width=\paperwidth, height=\@headerheight, keepaspectratio=false]{\@headerimg}
        \end{beamercolorbox}
    \fi
}

\def\@footerimgA{}
\def\@footerimgB{}
\def\@footerimgC{}

\newcommand{\setfooterimgs}[3]{%
    \def\@footerimgA{#1}%
    \def\@footerimgB{#2}%
    \def\@footerimgC{#3}%
}

\setbeamertemplate{footline}{
\ifx\@footerimgA\empty\else
    \begin{beamercolorbox}[wd=\paperwidth, ht=\@footerheight, dp=0cm, center]{}
        % O makebox força todo o conteúdo a ficar em uma única linha inquebrável
        \makebox[\paperwidth][c]{%
            % Imagem A
            \raisebox{0.1cm}{\includegraphics[height=\@footerheight, keepaspectratio]{\@footerimgA}}%
            % Verifica Imagem B
            \ifx\@footerimgB\empty\else
                \hspace{0.25cm}% Espaço Fixo entre A e B (ajuste se quiser mais perto/longe)
                \raisebox{0.1cm}{\includegraphics[height=\@footerheight, keepaspectratio]{\@footerimgB}}%
            \fi
            % Verifica Imagem C
            \ifx\@footerimgC\empty\else
                \hspace{0.25cm}% Espaço Fixo entre B e C
                \raisebox{0.1cm}{\includegraphics[height=\@footerheight, keepaspectratio]{\@footerimgC}}%
            \fi
        }%
    \end{beamercolorbox}
\fi
}

% --- 7. CAPA AUTOMATIZADA ---
\setbeamertemplate{title page}{
    \vspace*{0.4cm} 
    \begin{center}
        {\large \textbf{\inserttitle}\par} 
        \vspace{0.4cm}
        {\normalsize \insertauthor\par}
        \vspace{0.2cm}
        {\scriptsize \insertinstitute\par}
    \end{center}
    \vfill
    \begin{minipage}[b]{\textwidth}
        \begin{minipage}[c]{0.3\textwidth}
            \centering\ifx\@logoEsq\empty\else\@logoEsq\fi
        \end{minipage}\hfill
        \begin{minipage}[c]{0.3\textwidth}
            \centering\ifx\@logoMeio\empty\else\@logoMeio\fi
        \end{minipage}\hfill
        \begin{minipage}[c]{0.3\textwidth}
            \centering\ifx\@logoDir\empty\else\@logoDir\fi
        \end{minipage}
    \end{minipage}
    \vspace*{0.1cm}
}

% --- 8. AJUSTE FINO DO FRAMETITLE ---
\setbeamerfont{frametitle}{size=\normalsize, series=\bfseries} 
\setbeamertemplate{frametitle}{
    \vspace*{0.2cm} 
    \noindent{\usebeamerfont{frametitle}\insertframetitle}
    \par\vspace*{-0.1cm} 
}

% --- 9. MACROS DE CONTEÚDO ---
\newcommand{\imprimirfonte}[1]{%
    \ifstrempty{#1}{}{\par\vspace{0.02cm}{\tiny\noindent Fonte: #1\par}}%
}

\newcommand{\inserirfigura}[5][width=\linewidth]{
    \begin{figure}[H]
        \vspace*{-0.2cm} 
        \caption{#3}
        \centering
        \includegraphics[height=0.78\textheight, keepaspectratio, #1]{#2}
        \label{#5}
        \imprimirfonte{#4}
        \vspace*{-0.2cm} 
    \end{figure}
}

\newcommand{\inserirtabela}[4]{
    \begin{table}[H]
        \vspace*{-0.2cm}
        \caption{#1}
        \centering
        #3
        \label{#2}
        \imprimirfonte{#4}
        \vspace*{-0.2cm}
    \end{table}
}