# DP5 Workshop — Deluxe Paint 5 Clone
**Build 292** | Part of [Img Factory 1.6](https://github.com/X-Seti/Img-Factory-1.6)

A PyQt6 bitmap editor inspired by Deluxe Paint 5, with retro platform support.

## Usage

### Standalone
```bash
python3 dp5_workshop.py
```

### Drop-in for Img Factory 1.6
Copy this folder (`DP5_Workshop/`) into `apps/components/DP5_Workshop/` inside an Img Factory 1.6 installation.

## Requirements
```bash
pip install PyQt6 Pillow
```

## Features

**Tools:** Pencil, Eraser, Fill, Spray, Line, Rect, Circle, Triangle, Star, Polygon, Lasso, Select, Move, Picker, Text, Dither, Symmetry, Zoom (In/Out/Box/Fit)

**Platform Modes:** Amiga OCS/ECS/AGA/HAM6/HAM8/RTG, C64, ZX Spectrum, ZX80 (B&W), ZX81 WRX (Bayer dither), ZX Next, MSX1, Amstrad CPC, Atari ST, Atari 800, Plus/4, VIC-20

**User Palettes (42 presets):** Amiga · Commodore · Sinclair/ZX · Atari · Amstrad · Acorn · Tandy/Dragon · MSX · Nintendo · Sega · NEC · Other

**Import:** PNG/BMP/JPEG/WebP, TIFF, GIF (animated), TGA, PCX, DDS, PSD, IFF ILBM (8-bit/24-bit/HAM/EHB), Amiga .info (Classic/NewIcon), ICO, ICNS, SVG, ZX SCR, MSX SC2, Atari PI1, C64 Koala/Art Studio, ZX Next NXI

**Export:** PNG, BMP, TGA, DDS, PCX, IFF ILBM/HAM, ZX SCR/TAP, ZX Next NXI/NEX, MSX SC2/COM, Atari PI1, C64/C64M/Plus4/VIC20 PRG, ICO, ICNS, Amiga .info, SVG

**Batch Convert:** Icons (info/ico/icns/png/svg) and Textures (with resize + power-of-two snap)

**Render As:** ASCII art, ANSI block art, PETSCII (C64), Teletext mosaic

**Animation:** Frame timeline, onion skin, GIF import/export, PNG sequence

---
Repo: https://github.com/X-Seti/Deluxe-Paint-Clone---Img-Factory
