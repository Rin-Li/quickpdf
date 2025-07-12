# mdclip

## ✨ Purpose

This tool was built out of a personal need.

When creating academic presentations, I often need to insert **a large number of small, high-quality math formulas** into PowerPoint on macOS.
 However, macOS PowerPoint’s built-in equation editor is limited and sometimes fails to render certain LaTeX commands properly.

In contrast, typing formulas in Markdown is often faster and cleaner — especially with help from GPT or snippet tools — and in most cases I only need **simple inline expressions**, not full LaTeX environments.

So I built **`mdclip`**, a small utility that lets you:

- Write Markdown with LaTeX-style math like:
  `I want to add the $a + b = 2$.` or `$WR \in \mathbb{R}_{+}^{m \times r}, \quad R^\top H \in \mathbb{R}_{+}^{r \times n}$`
- Automatically render it as a **clean, tightly-cropped PDF**
- Copy the result directly to your clipboard, ready to paste into PowerPoint

> ⚠️ Note: This tool currently supports only **simple single-line formulas** using `$...$`. Multi-line equations and complex LaTeX environments are not supported (yet).



## ⚙️ Setup

```bash
cd quickpdf
pip install -r requirements.txt
brew install --cask mactex-no-gui
```

> macOS will ask for permissions the first time.
> Go to **System Settings → Privacy & Security → Accessibility**, and enable access for **Terminal**.



## 🚀 Run the Daemon

Start the background listener with:

```bash
python -m scripts.mdclip_daemon
```

This will run `mdclip` as a background service, watching your clipboard for Markdown input.

Once running, the usage is as simple as:

1. **Command + L** — to generate a cropped PDF from the clipboard content
2. **Command + C** — to paste the rendered formula directly into PowerPoint

> 🛠️ You can customize the hotkey (default: `Command + L`) in
> `mdclip/runtime/hotkey_listener.py`.

