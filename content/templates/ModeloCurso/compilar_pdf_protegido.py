#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compilador LaTeX com Proteção Automática por Senha (.tex -> PDF Protegido).
Desenvolvido para o ecossistema ReLaTeX - IFF Campus Bom Jesus do Itabapoana.
Professor Responsável: Prof. Dr. Pedro Henrique Rocha de Andrade

Funcionamento:
1. Recebe um ou mais arquivos '.tex'.
2. Compila automaticamente via 'pdflatex', 'lualatex' ou 'xelatex' (2 passagens).
3. Após gerar o PDF, aplica a criptografia com a senha padrão (padrão: 'escritaiff2026').
4. Remove arquivos temporários da compilação (.aux, .log, .nav, .snm, .toc, .out).

Uso:
  python3 scripts/compilar_pdf_protegido.py aula-01.tex --senha escritaiff2026
  python3 scripts/compilar_pdf_protegido.py *.tex
"""

import os
import sys
import glob
import shutil
import argparse
import subprocess
from pypdf import PdfReader, PdfWriter

def compile_and_encrypt(tex_file, password="escritaiff2026", engine="pdflatex", keep_temps=False):
    if not os.path.exists(tex_file):
        print(f"[ERRO] Arquivo não encontrado: {tex_file}")
        return False

    abs_tex = os.path.abspath(tex_file)
    cwd = os.path.dirname(abs_tex)
    base_name = os.path.splitext(os.path.basename(tex_file))[0]
    pdf_path = os.path.join(cwd, f"{base_name}.pdf")

    print(f"[{base_name}] 1/3 Compilando LaTeX com '{engine}'...")
    cmd = [engine, "-interaction=nonstopmode", "-halt-on-error", os.path.basename(tex_file)]
    
    # 2 passagens para garantir referências cruzadas e paginação
    for p in range(2):
        res = subprocess.run(cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if res.returncode != 0 and not os.path.exists(pdf_path):
            print(f"[ERRO] Falha na compilação do arquivo '{tex_file}':")
            print(res.stdout.decode("utf-8", errors="ignore")[-1000:])
            return False

    if not os.path.exists(pdf_path):
        print(f"[ERRO] Arquivo PDF não foi gerado: {pdf_path}")
        return False

    print(f"[{base_name}] 2/3 Aplicando criptografia institucional com senha padrão...")
    try:
        reader = PdfReader(pdf_path)
        writer = PdfWriter()
        writer.append_pages_from_reader(reader)
        writer.encrypt(password)
        
        # Salva o PDF criptografado (sobrescreve o original gerado)
        with open(pdf_path, "wb") as f_out:
            writer.write(f_out)
        print(f"[{base_name}] SUCESSO! PDF protegido gravado em: {pdf_path}")
    except Exception as e:
        print(f"[ERRO] Falha ao criptografar o PDF '{pdf_path}': {e}")
        return False

    if not keep_temps:
        print(f"[{base_name}] 3/3 Limpando arquivos temporários...")
        for ext in [".aux", ".log", ".nav", ".out", ".snm", ".toc", ".vrb", ".fls", ".fdb_latexmk"]:
            tmp_file = os.path.join(cwd, f"{base_name}{ext}")
            if os.path.exists(tmp_file):
                try:
                    os.remove(tmp_file)
                except Exception:
                    pass

    return True

def main():
    parser = argparse.ArgumentParser(description="Compila arquivos .tex para PDF já com senha padrão")
    parser.add_argument("arquivos", nargs="+", help="Arquivos .tex para compilar (suporta glob *.tex)")
    parser.add_argument("--senha", default="escritaiff2026", help="Senha padrão do PDF (default: escritaiff2026)")
    parser.add_argument("--engine", default="pdflatex", choices=["pdflatex", "lualatex", "xelatex"], help="Compilador LaTeX")
    parser.add_argument("--keep", action="store_true", help="Não apagar arquivos auxiliares (.aux, .log, etc.)")
    args = parser.parse_args()

    sucesso = 0
    falhas = 0

    for padrao in args.arquivos:
        for tex_file in glob.glob(padrao):
            if compile_and_encrypt(tex_file, password=args.senha, engine=args.engine, keep_temps=args.keep):
                sucesso += 1
            else:
                falhas += 1

    print(f"\nResumo da Operação: {sucesso} PDF(s) gerados e protegidos por senha | {falhas} falha(s).")
    if falhas > 0:
        sys.exit(1)

if __name__ == "__main__":
    main()
