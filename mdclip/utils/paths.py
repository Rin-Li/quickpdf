import os
import tempfile
from pathlib import Path

DEBUG = bool(os.getenv("MDCLIP_DEBUG"))

def get_tmpdir() -> Path:
    if DEBUG:
        p = Path("/tmp/mdclip_debug")
        p.mkdir(parents=True, exist_ok=True)
        print(f"Debug temp dir: {p}")
        return p
    return Path(tempfile.mkdtemp())