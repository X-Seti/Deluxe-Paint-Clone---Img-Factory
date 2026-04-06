# DP5 Workshop

**Deluxe Paint 5 inspired bitmap paint editor** — standalone application and embeddable PyQt6 component.

Part of the [IMG Factory 1.6](https://github.com/X-Seti/Img-Factory-1.6) GTA modding tool suite, but fully usable on its own.

---

## Features

### Tools
- **Pencil** — freehand pixel drawing with configurable brush size
- **Eraser** — erase to transparent
- **Flood Fill** — 4-connected colour fill
- **Airbrush / Spray** — randomised spray paint effect
- **Colour Picker** — sample any pixel from the canvas
- **Straight Line** — with endpoint handles
- **Bézier Curve** — click to place control points, double-click to commit
- **Rectangle** — outline or filled (right-click button to toggle)
- **Ellipse** — outline or filled (right-click to toggle)
- **Triangle** — outline or filled
- **Polygon** — N-sided, click vertices, double-click to close; right-click fills
- **Star** — 5-point, outline or solid
- **Lasso** — freehand selection; right-click fills the enclosed area
- **Marquee Select** — drag to select, drag inside to lift and move as a floating object
- **Stamp / Brush** — paste the copy buffer anywhere by clicking; ghost preview follows cursor
- **Zoom** — click to zoom in, right-click to zoom out; Ctrl+scroll zooms to cursor
- **Text** — click canvas to place text with font size choice

### Selection & Objects
- Cut (Ctrl+X), Copy (Ctrl+C), Paste (Ctrl+V) — paste enters stamp mode, click to place
- Drag inside a selection to **lift and move** as a floating object
- Arrow keys nudge floating object 1 px (Shift = 10 px)
- Enter to stamp permanently; Escape to cancel and restore
- Brush Thumbnail — shows copy buffer; click to enter stamp mode, right-click to clear

### Canvas & View
- Zoom 0.05× – 16×, anchored to cursor position
- Scrollbars appear automatically when zoomed in
- Spacebar + drag = temporary pan with any tool
- Pixel grid overlay at zoom ≥ 4×
- Auto-fit zoom on image open

### Palettes
- **Image palette** — auto-extracted from opened image (up to 256 colours)
- **Retro presets** — Amiga OCS/AGA/WB, C64, ZX Spectrum, Amstrad CPC, Atari 800, Atari 2600 NTSC, ULA Plus
- FG / BG colour swatches with swap (X key or double-click)

### Brush Manager
- Save any copy buffer as a named PNG brush
- Load, delete, and import brushes
- Stored in `~/.config/imgfactory/dp5_brushes/`

### File I/O
- Load / Save PNG
- Import / Export (IFF ILBM, BMP, JPEG, and more via Pillow)
- Add images to the bitmap list for multi-image sessions

### Picture Operations
- Flip horizontal / vertical
- Rotate 90°CW, 90°CCW, 180°, arbitrary angle
- Scale canvas with resampling options (Nearest, Bilinear, Bicubic, Lanczos)
- Invert colours, Brighten +25, Darken −25

### IMG Factory Integration
- Docks as a tab in IMG Factory 1.6 (`open_dp5_workshop_docked()`)
- Opened from the **Paint Edit** button in the right panel
- TXD Workshop **Paint** button opens the selected texture directly in DP5 Workshop; edited RGBA is written back on **Apply to Texture**

---

## Requirements

- Python 3.10+
- PyQt6
- Pillow

```bash
pip install PyQt6 Pillow
```

---

## Running standalone

```bash
python3 dp5_workshop.py
```

Or with a file:

```bash
python3 dp5_workshop.py image.png
```

---

## Embedding in another PyQt6 app

```python
from dp5_workshop import DP5Workshop, open_dp5_workshop

# As a docked widget inside a tab
workshop = DP5Workshop(parent_widget, main_window)
workshop.setWindowFlags(Qt.WindowType.Widget)
tab_widget.addTab(workshop, "DP5 Paint")

# Or as a standalone window
workshop = open_dp5_workshop()
```

To pre-load an image by path:

```python
workshop._import_bitmap_path("/path/to/image.png")
```

---

## Keyboard shortcuts

| Key | Action |
|-----|--------|
| P | Pencil |
| E | Eraser |
| F | Flood fill |
| S | Airbrush |
| K | Colour picker |
| Q | Bézier curve |
| L | Line |
| R | Rectangle |
| C | Ellipse |
| T | Triangle |
| O | Polygon |
| `*` | Star |
| M | Marquee select |
| G | Lasso |
| Z | Zoom |
| I | Text |
| X | Swap FG/BG |
| Ctrl+Z | Undo |
| Ctrl+Y | Redo |
| Ctrl+C | Copy selection |
| Ctrl+X | Cut selection |
| Ctrl+V | Paste (enters stamp mode) |
| Ctrl+A | Select all |
| Enter | Stamp floating object |
| Esc | Cancel / exit stamp mode |
| Arrow keys | Nudge float (1px) or scroll |
| Shift+Arrow | Nudge float (10px) or fast scroll |
| Ctrl+scroll | Zoom to cursor |
| Space+drag | Temporary pan |
| Middle drag | Pan |

Right-click shape buttons (Rect, Ellipse, Triangle, Polygon, Star, Lasso) to toggle outline ↔ filled.

---

## Settings

Stored at `~/.config/imgfactory/dp5_workshop.json`:

| Key | Default | Description |
|-----|---------|-------------|
| `tool_icon_size` | 42 | Gadget button size in pixels (24–64) |
| `tool_columns` | 0 | Gadget bar columns (0=auto, 2/3/4) |
| `default_zoom` | 4 | Startup zoom level |
| `default_width` | 320 | New canvas width |
| `default_height` | 200 | New canvas height |
| `undo_levels` | 32 | Undo stack depth |
| `show_pixel_grid` | true | Show grid at zoom ≥4× |
| `retro_palette` | Amiga OCS | Default user palette preset |

---

## License

[MIT](LICENSE) — © 2026 X-Seti
