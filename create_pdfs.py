#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Kreiraj PDF verzije markdown fajlova koriscenjem Pandoc
Ako PDF engine nije dostupan, kreiraj HTML verzije
"""

import os
import subprocess
from pathlib import Path

def create_pdfs_or_html():
    pdf_dir = Path("pdf")
    pdf_dir.mkdir(exist_ok=True)

    md_files = [
        ("README.md", "README"),
        ("CONTRIBUTING.md", "CONTRIBUTING"),
        ("ORGANIZACIJA_PROJEKTA.md", "ORGANIZACIJA_PROJEKTA"),
        ("PRAVNA_ZASNOVA_JAVNE_OBJAVE.md", "PRAVNA_ZASNOVA_JAVNE_OBJAVE"),
        ("prijave/README.md", "PRIJAVE_README"),
        ("prijave/PRIJAVA_I_KORUPCIJA.md", "PRIJAVA_I_KORUPCIJA"),
        ("prijave/PRIJAVA_II_ORGANIZOVANI_KRIMINAL.md", "PRIJAVA_II_ORGANIZOVANI_KRIMINAL"),
        ("prijave/PRIJAVA_III_POLITICKA_ODGOVORNOST.md", "PRIJAVA_III_POLITICKA_ODGOVORNOST"),
        ("prijave/PRIJAVA_IV_EU_FONDOVI_MEDJUNARODNO.md", "PRIJAVA_IV_EU_FONDOVI_MEDJUNARODNO"),
        ("prijave/PRILOG_LEGAL_APPENDIX_EVIDENCE.md", "PRILOG_LEGAL_APPENDIX_EVIDENCE"),
        ("prijave/SCREENSHOT_EVIDENCE_MANIFEST.md", "SCREENSHOT_EVIDENCE_MANIFEST"),
        ("public/README.md", "PUBLIC_README"),
    ]

    print("\nKreiram HTML/PDF verzije markdown fajlova...\n")
    print("=" * 70)

    success_count = 0

    for md_file, name in md_files:
        md_path = Path(md_file)

        if not md_path.exists():
            print("[PRESKOCENO] " + md_file + " - fajl ne postoji")
            continue

        # Prvo pokusaj sa PDF
        pdf_path = pdf_dir / (name + ".pdf")
        html_path = pdf_dir / (name + ".html")

        # Komanda za pandoc - prvo HTML sa CSS
        pandoc_html_cmd = [
            "pandoc",
            str(md_path),
            "-o", str(html_path),
            "--standalone",
            "--css", "https://cdn.jsdelivr.net/npm/github-markdown-css@4.0.0/github-markdown-light.css",
            "--variable", "lang=sr"
        ]

        # Pokusaj sa PDF-om prvo
        pandoc_pdf_cmd = [
            "pandoc",
            str(md_path),
            "-o", str(pdf_path),
            "--variable", "lang=sr"
        ]

        print("[KONVERTUJ] " + md_file)

        # Pokusaj PDF
        pdf_result = subprocess.run(pandoc_pdf_cmd, capture_output=True, text=True)

        if pdf_result.returncode == 0:
            print("           -> [PDF] " + name + ".pdf")
            success_count += 1
        else:
            # Ako PDF ne uspe, kreiraj HTML
            html_result = subprocess.run(pandoc_html_cmd, capture_output=True, text=True)
            if html_result.returncode == 0:
                print("           -> [HTML] " + name + ".html")
                success_count += 1
            else:
                print("           -> [GRESKA]")

    print("=" * 70)
    print("[REZULTAT] " + str(success_count) + " od " + str(len(md_files)) + " konvertovano")
    print("[LOKACIJA] " + str(pdf_dir.absolute()) + "\n")

if __name__ == "__main__":
    create_pdfs_or_html()
