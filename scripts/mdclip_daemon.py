from mdclip.runtime.hotkey_listener import start_listener
from mdclip.runtime.worker import run_forever
import threading, signal, sys

def main():
    th = threading.Thread(target=run_forever, daemon=True)
    print("mdclip_daemon starting...")
    th.start()
    start_listener()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, lambda s,f: sys.exit(0))
    main()
