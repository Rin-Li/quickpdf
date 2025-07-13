from datetime import datetime
from pathlib import Path
from typing import Optional
from mdclip.utils.cmd import run_cmd

PANDOC_CMD = [
    "pandoc", "--standalone", "--pdf-engine=xelatex",
    "-V", "documentclass=standalone"
]
PDFCROP_CMD = ["pdfcrop", "--margins", "0"]

def convert_md_to_pdf(md_text: str, output_pdf: Optional[str] = None) -> Path:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_dir = Path.cwd() / "tmp" / f"mdclip_{ts}"
    base_dir.mkdir(parents=True, exist_ok=True)

    md = base_dir / "input.md"
    tex = base_dir / "output.tex"
    raw = base_dir / "output.pdf"
    final_pdf = base_dir / "result.pdf" if output_pdf is None else Path(output_pdf).expanduser().resolve()

    md.write_text(md_text, encoding="utf-8")

    run_cmd(PANDOC_CMD + [str(md), "-o", str(tex)])

    run_cmd([
        "xelatex",
        "-interaction=nonstopmode",
        "-halt-on-error",
        "-file-line-error",
        "-output-directory", str(base_dir),
        str(tex)
    ])

    run_cmd(PDFCROP_CMD + [str(raw), str(final_pdf)])

    print(f" PDF generated at: {final_pdf}")
    return final_pdf
