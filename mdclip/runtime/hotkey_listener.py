"""mdclip.runtime.hotkey_listener

Global hot‑key listener (⌘ + L) that:
1. Simulates ⌘C to copy current selection.
2. Reads clipboard Markdown.
3. Converts it to a cropped PDF.
4. Copies the PDF back to clipboard so you can ⌘V in PPT/Keynote.

Requires the hosting app (Terminal/iTerm/pyinstaller‑packed app) to have
macOS Accessibility permission so that it can listen for keys *and* send
synthetic ⌘C key‑presses.
"""

from __future__ import annotations

import time
from subprocess import check_output, run

from pynput import keyboard

from mdclip.core.converter import convert_md_to_pdf
from mdclip.core.clipboard import copy_pdf_to_clipboard

HOTKEY = '<cmd>+l'  # ⌘ + L, change if you like


def _simulate_copy() -> None:
    """Tell System Events to send ⌘C to foreground app (copies selection)."""
    try:
       run([
            'osascript',
            '-e', 'tell application "System Events" to keystroke "c" using command down',
        ], timeout=2, capture_output=True, text=True) 
    except Exception as e:
        print(f"AppleScript execution failed: {e}")
        

def _on_hotkey():
    print("Hotkey triggered – copying selection …")

    _simulate_copy()
    time.sleep(0.2)  # wait for clipboard to update
    md_text = check_output('pbpaste', text=True)
    if not md_text.strip():
        print('Clipboard is empty or not text – abort')
        return

    print(f'Markdown read ({len(md_text)} chars). Converting …')
    try:
        pdf_path = convert_md_to_pdf(md_text)
        copy_pdf_to_clipboard(pdf_path)
        print(f'PDF copied to clipboard: {pdf_path}')
    except Exception as exc:
        print(f'Conversion failed: {exc}')


def start_listener() -> None:  # called by mdclip_daemon
    print(f'⌨️  Listening for hotkey {HOTKEY} (press to convert selection)')
    with keyboard.GlobalHotKeys({HOTKEY: _on_hotkey}) as listener:
        listener.join()

# run standalone for debugging
if __name__ == '__main__':
    start_listener()
