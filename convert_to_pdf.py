#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Konvertuj Markdown fajlove u PDF sa srpskim podrškom
Koristi Pandoc + pdfkit ili direktno sa pandoc HTML rendering
"""

import os
import sys
import subprocess
from pathlib import Path

# UTF-8 podrška za Windows
if sys.platform == 'win32':
    os.environ['PYTHONIOENCODING'] = 'utf-8'

def convert_with_pandoc_html_css(md_file, pdf_file):
    """Konvertuj markdown u PDF kroz HTML sa CSS"""
    try:
        # Template HTML sa CSS za PDF
        html_template = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        @page {{
            size: A4;
            margin: 20mm;
            margin-bottom: 30mm;
            @bottom-right {{
                content: "Strana " counter(page) " od " counter(pages);
            }}
        }}
        body {{
            font-family: 'Calibri', 'Arial', sans-serif;
            line-height: 1.6;
            color: #333;
            padding: 0;
            margin: 0;
        }}
        h1 {{
            font-size: 2em;
            color: #000;
            border-bottom: 3px solid #333;
            padding-bottom: 10px;
            margin-top: 1.5em;
            margin-bottom: 0.5em;
            page-break-after: avoid;
        }}
        h2 {{
            font-size: 1.5em;
            color: #222;
            border-bottom: 2px solid #666;
            padding-bottom: 8px;
            margin-top: 1.3em;
            margin-bottom: 0.4em;
            page-break-after: avoid;
        }}
        h3 {{
            font-size: 1.2em;
            color: #333;
            margin-top: 1em;
            margin-bottom: 0.3em;
            page-break-after: avoid;
        }}
        h4, h5, h6 {{
            font-size: 1em;
            color: #444;
            page-break-after: avoid;
        }}
        p {{
            margin: 0.5em 0;
            text-align: justify;
        }}
        ul, ol {{
            margin: 0.5em 0;
            padding-left: 2em;
        }}
        li {{
            margin: 0.3em 0;
            line-height: 1.5;
        }}
        pre {{
            background-color: #f5f5f5;
            padding: 12px;
            border-left: 4px solid #ccc;
            border-radius: 4px;
            overflow-x: auto;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
            margin: 1em 0;
            page-break-inside: avoid;
        }}
        code {{
            font-family: 'Courier New', monospace;
            background-color: #f0f0f0;
            padding: 2px 5px;
            border-radius: 3px;
            font-size: 0.95em;
        }}
        pre code {{
            background-color: transparent;
            padding: 0;
            font-size: 0.9em;
        }}
        blockquote {{
            border-left: 4px solid #ddd;
            margin: 1em 0;
            padding-left: 1em;
            color: #666;
            page-break-inside: avoid;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 1em 0;
            page-break-inside: avoid;
        }}
        table, th, td {{
            border: 1px solid #bbb;
            padding: 8px 10px;
        }}
        th {{
            background-color: #f0f0f0;
            font-weight: bold;
            text-align: left;
        }}
        tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}
        a {{
            color: #0066cc;
            text-decoration: none;
            word-break: break-word;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        strong, b {{
            font-weight: bold;
            color: #222;
        }}
        em, i {{
            font-style: italic;
        }}
        .page-break {{
            page-break-after: always;
        }}
        hr {{
            border: none;
            border-top: 1px solid #ccc;
            margin: 1.5em 0;
            page-break-after: avoid;
        }}
        img {{
            max-width: 100%;
            height: auto;
        }}
        .emoji {{
            font-family: 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', sans-serif;
        }}
    </style>
</head>
<body>
{content}
</body>
</html>"""

        # Konvertuj markdown u HTML korišćenjem pandoc
        temp_html = str(pdf_file).replace('.pdf', '_temp.html')

        pandoc_cmd = [
            'pandoc',
            str(md_file),
            '-o', temp_html,
            '--from', 'markdown',
            '--to', 'html',
            '--variable', 'lang=sr'
        ]

        result = subprocess.run(pandoc_cmd, capture_output=True, text=True)

        if result.returncode != 0:
            print("  [GREŠKA] Pandoc: " + result.stderr[:100])
            return False

        # Čitaj HTML koji je generisao pandoc
        with open(temp_html, 'r', encoding='utf-8') as f:
            pandoc_html = f.read()

        # Wydvoji sadržaj iz body-ja
        import re
        body_match = re.search(r'<body[^>]*>(.*?)</body>', pandoc_html, re.DOTALL)
        content = body_match.group(1) if body_match else pandoc_html

        # Napravi finalni HTML sa CSS
        final_html = html_template.format(content=content)

        # Sačuvaj finalni HTML
        final_html_file = str(pdf_file).replace('.pdf', '.html')
        with open(final_html_file, 'w', encoding='utf-8') as f:
            f.write(final_html)

        # Konvertuj HTML u PDF koristeći pandoc (ako ima PDF engine)
        pdf_cmd = [
            'pandoc',
            final_html_file,
            '-o', str(pdf_file),
            '--from', 'html',
            '--to', 'pdf'
        ]

        pdf_result = subprocess.run(pdf_cmd, capture_output=True, text=True)

        # Cleanup
        if os.path.exists(temp_html):
            os.remove(temp_html)
        if os.path.exists(final_html_file):
            os.remove(final_html_file)

        if pdf_result.returncode == 0:
            return True
        else:
            print("  [UPOZORENJE] PDF engine: " + pdf_result.stderr[:100])
            # Pokušaj sa pdfkit ako je dostupan
            try:
                import pdfkit
                pdfkit.from_file(final_html_file, str(pdf_file))
                return True
            except:
                return False

    except Exception as e:
        print("  [GREŠKA]: " + str(e)[:100])
        return False

def main():
    # Kreiraj pdf folder ako ne postoji
    pdf_dir = Path("pdf")
    pdf_dir.mkdir(exist_ok=True)

    # Lista markdown fajlova
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

    print("\n" + "="*70)
    print("Konvertovanje Markdown fajlova u PDF")
    print("="*70 + "\n")

    successful = 0
    failed = 0

    for md_file, pdf_name in md_files:
        md_path = Path(md_file)

        if not md_path.exists():
            print("[GREŠKA] Fajl ne postoji: " + md_file)
            continue

        pdf_path = pdf_dir / f"{pdf_name}.pdf"

        print("[KONVERTUJ] " + md_file.ljust(50) + " -> " + pdf_name + ".pdf")

        if convert_with_pandoc_html_css(str(md_path), str(pdf_path)):
            print("   [OK]\n")
            successful += 1
        else:
            print("   [GREŠKA]\n")
            failed += 1

    print("="*70)
    print("[REZULTAT] " + str(successful) + " uspešno, " + str(failed) + " neuspešno")
    print("[LOKACIJA] PDF fajlovi se nalaze u: " + str(pdf_dir.absolute()))
    print("="*70 + "\n")

if __name__ == "__main__":
    main()
