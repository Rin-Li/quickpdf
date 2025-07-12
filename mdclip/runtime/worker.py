from queue import Queue
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from mdclip.core.converter import convert_md_to_pdf
from mdclip.core.clipboard import copy_pdf_to_clipboard
from mdclip.utils.paths import DEBUG

_q = Queue(maxsize=3)
_pool = ThreadPoolExecutor(max_workers=1)  

def add_task(md_text: str) -> None:
    _q.put(md_text)

def _job(md_text: str):
    try:
        pdf = convert_md_to_pdf(md_text)
        copy_pdf_to_clipboard(pdf)
        print(f" Copied PDF → {pdf}")
    except Exception as e:
        print(f"{e}")

def run_forever():
    while True:
        txt = _q.get()
        _pool.submit(_job, txt)

if __name__ == "__main__":        
    if DEBUG:
        print("⚙️  mdclip worker (DEBUG)")
    run_forever()
