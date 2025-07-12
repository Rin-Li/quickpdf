from pathlib import Path
from mdclip.utils.cmd import run_cmd

def copy_pdf_to_clipboard(pdf: Path) -> None:
    script = f'set theFile to POSIX file "{pdf}" as alias\n' \
             f'set the clipboard to (read theFile as «class PDF »)'
    run_cmd(["osascript", "-e", script])
