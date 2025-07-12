import subprocess

def run_cmd(cmd: list[str]) -> None:
    """Run shell command and raise on non-zero exit."""
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if proc.returncode != 0:
        raise RuntimeError(
            f"Command {' '.join(cmd)} failed ({proc.returncode}):\n{proc.stderr.strip()}"
        )