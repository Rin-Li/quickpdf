from datetime import datetime
from pathlib import Path
from typing import Optional
from mdclip.utils.cmd import run_cmd
from mdclip.utils.paths import get_tmpdir

PANDOC_CMD = ["pandoc", "--standalone", "--pdf-engine=xelatex", "-V", "documentclass=standalone"]
PDFCROP_CMD = ["pdfcrop"]

def convert_md_to_pdf(md_text: str, output_pdf: Optional[str]=None) -> Path:
    tmpdir = get_tmpdir()
    md = tmpdir / "input.md"
    tex = tmpdir / "output.tex"
    raw = tmpdir / "output.pdf"

    md.write_text(md_text, encoding="utf-8")
    run_cmd(PANDOC_CMD + [str(md), "-o", str(tex)])
    run_cmd(["xelatex", "-interaction=nonstopmode", "-output-directory", str(tmpdir), str(tex)])

    if output_pdf is None:
        tmp_dir = Path.cwd() / "tmp"
        tmp_dir.mkdir(exist_ok=True)
        
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_pdf = tmp_dir / f"mdclip_{ts}.pdf"
    cropped = Path(output_pdf).expanduser().resolve()
    run_cmd(PDFCROP_CMD + [str(raw), str(cropped)])
    return cropped