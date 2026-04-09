# DP5 Workshop

**Deluxe Paint 5 inspired bitmap paint editor** — standalone application and embeddable PyQt6 component.

Part of the [IMG Factory 1.6](https://github.com/X-Seti/Img-Factory-1.6) GTA modding tool suite, but fully usable on its own.

Current build: **267a** — April 2026

---

## Features

### Tools
- **Pencil** — freehand pixel drawing with configurable brush size
- **Eraser** — erase to transparent or background colour
- **Flood Fill** — 4-connected colour fill
- **Airbrush / Spray** — randomised spray paint effect
- **Colour Picker** — sample any pixel from the canvas
- **Straight Line** — with endpoint handles
- **Bézier Curve** — click to place control points, double-click to commit
- **Rectangle** — outline or filled (right-click to toggle)
- **Ellipse** — outline or filled (right-click to toggle)
- **Triangle** — outline or filled
- **Polygon** — N-sided, click vertices, double-click to close; right-click fills
- **Star** — 5-point, outline or solid
- **Lasso** — freehand selection; right-click fills the enclosed area
- **Marquee Select** — drag to select, drag inside to lift and move as floating object
- **Stamp / Brush** — paste copy buffer by clicking; ghost preview follows cursor
- **Zoom** — click to zoom in, right-click to zoom out; Ctrl+scroll to cursor
- **Text** — click canvas to place text
- **Crop** — crop canvas to current selection
- **Resize** — resize with width, height, bit depth and resampling in one dialog
- **Dither** — cycles: checkerboard → Bayer 4×4 → off
- **Symmetry** — cycles: H → V → Quad → off

### New Canvas
- Platform preset list: Amiga LowRes/HiRes, C64 Hires/Multi, ZX Spectrum, ZX Next 256/320, MSX1, Amstrad CPC, Atari ST, Plus/4, VIC-20, Sinclair QL, icons, sprites, HD, 4K
- Bit depth: 32-bit RGBA, 24-bit RGB, 16-bit R5G6B5, 8-bit indexed
- Fill colour: grey, black, white, transparent

### Palettes
- **Image palette** — auto-extracted from opened image (up to 256 colours)
- **Retro presets**: Amiga OCS/AGA/AGA WB, C64, ZX Spectrum, Amstrad CPC, Atari 800, Atari 2600 NTSC, ULA Plus, MSX1, Atari ST, Plus/4, VIC-20, Sinclair QL
- **Colour history** — last 12 used colours as swatches
- FG / BG swatches with swap; Opacity slider
- Image palette: bit-depth quantize + hue-sort Group button

### Platform Mode
- Platform menu: None, Amiga, C64, C64M, ZX Spectrum, ZX Next, MSX1, Amstrad CPC, Atari ST
- Auto-loads correct platform palette
- Cell grid overlay shows platform cell boundaries
- Colour constraint enforcement per platform (e.g. 2 colours per 8×8 cell for C64)

### Dither (Picture menu — whole canvas)
- Floyd-Steinberg error diffusion
- Bayer 4×4 ordered dither
- Checkerboard FG/BG

### File I/O
- Load / Save PNG, Export IFF ILBM
- **Import**: ZX Spectrum SCR, MSX SC2, Atari ST PI1, C64 Koala, C64 Art Studio, ZX Next NXI, ZX Next PAL
- **Export**: ZX Spectrum SCR, MSX SC2, Atari ST PI1, C64 Koala, C64 Art Studio, ZX Next NXI, ZX Next PAL
- **Executables**: ZX Spectrum TAP, ZX Next NEX, C64 PRG (hires+multi), MSX COM, Plus/4 PRG, VIC-20 PRG

### Picture Operations
- Flip H/V, Rotate 90°/180°/arbitrary, Scale, Invert, Brighten, Darken
- Dither canvas (Floyd-Steinberg, Bayer, Checkerboard)

### Custom Tool Icons
- Drop PNG or SVG into `icons/` folder named by tool ID
- Falls back to built-in SVG icons automatically

---

## Requirements

```bash
pip install PyQt6 Pillow
```

---

## Running standalone

```bash
python3 dp5_workshop.py
python3 dp5_workshop.py image.png
```

---

## Embedding

```python
from dp5_workshop import DP5Workshop, open_dp5_workshop

workshop = DP5Workshop(parent_widget, main_window)
tab_widget.addTab(workshop, "DP5 Paint")

# Pre-load image
workshop._import_bitmap_path("/path/to/image.png")
```

---

## Keyboard Shortcuts

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
| X | Crop tool |
| V | Resize dialog |
| D | Dither cycle |
| Y | Symmetry cycle |
| Ctrl+Z/Y | Undo/Redo |
| Ctrl+C/X/V | Copy/Cut/Paste |
| Ctrl+A | Select all |
| Enter | Stamp float |
| Esc | Cancel |
| Arrow | Nudge float 1px |
| Shift+Arrow | Nudge 10px |
| Ctrl+scroll | Zoom to cursor |
| Space+drag | Pan |

---

## Settings

Stored at `~/.config/imgfactory/dp5_workshop.json`:

| Key | Default | Description |
|-----|---------|-------------|
| `tool_icon_size` | 42 | Gadget size px (20–64) |
| `tool_columns` | 3 | Gadget columns (3–6) |
| `hidden_tools` | [] | Tool IDs to hide |
| `default_width` | 320 | New canvas width |
| `default_height` | 200 | New canvas height |
| `default_zoom` | 4 | Startup zoom |
| `undo_levels` | 32 | Undo depth |
| `show_pixel_grid` | true | Pixel grid at zoom ≥4× |
| `show_cell_grid` | false | Platform cell grid |
| `show_statusbar` | true | Status bar |
| `retro_palette` | Amiga AGA WB | Default user palette |
| `img_pal_cols` | 16 | Image palette columns |
| `img_pal_rows` | 16 | Image palette max rows |
| `user_pal_cols` | 16 | User palette columns |
| `user_pal_rows` | 16 | User palette max rows |
| `platform_mode` | none | Platform constraint mode |
| `menu_style` | topbar | topbar or dropdown |
| `ui_font_size` | 10 | UI font size |
| `zoom_to_fit_resize` | false | Fit on resize |

---

## License

[MIT](LICENSE) — © 2026 X-Seti
