# DP5 Workshop — Deluxe Paint 5 Clone
**Build 299** | Part of [Img Factory 1.6](https://github.com/X-Seti/Img-Factory-1.6)

A PyQt6 bitmap editor inspired by Deluxe Paint 5, with comprehensive retro platform support.

## Usage

### Standalone
```bash
python3 dp5_workshop.py
```

### Drop-in for Img Factory 1.6
Copy this folder into `apps/components/DP5_Workshop/` inside an Img Factory 1.6 installation.

## Requirements
```bash
pip install PyQt6 Pillow
```

## Features

### Drawing Tools
Pencil, Eraser, Fill, Spray, Line, Rect, Circle, Triangle, Star, Polygon,
Lasso, Select, Move, Picker, Text (inline — click canvas to type), Dither, Symmetry,
Zoom (In/Out/Box select/Fit)

### Platform Modes with colour constraints
**Amiga:** OCS PAL/NTSC, OCS HiRes 640×256, OCS interlace 320×512, ECS, AGA, HAM6, HAM8, RTG  
**Commodore:** C64, C64 Multicolour, VIC-20, Plus/4  
**Sinclair/ZX:** Spectrum 48K/128K, ZX80, ZX81 WRX, ZX Next L2/ULA, Timex TS2068, Timex HiRes 512×192, Pentagon, Jupiter Ace  
**Atari:** 2600, 800/XL/XE, 5200, 7800, ST, STe, Lynx, Falcon, Jaguar  
**Amstrad:** CPC Mode 0/1/2, CPC+, PCW, NC100/200  
**MSX:** MSX1, MSX2  
**Other:** RM Nimbus, NES, SNES, Game Boy/Color/Advance, Sega (SG-1000/MS/MD/GG), PC Engine

### User Palettes (48 presets, hierarchical menu)
Amiga · Commodore · Sinclair/ZX · Atari · Amstrad · Acorn ·
Tandy/Dragon · MSX · Nintendo · Sega · NEC · Other

All with accurate hardware colour spaces:
- 2-colour B&W (ZX80, Jupiter Ace)
- 4-colour (Game Boy, ZX Spectrum clash)
- 16-colour (C64, Spectrum, ST, NES)
- 27-colour (Amstrad CPC)
- 64-colour (Amiga ECS Extra Half-Brite)
- 128-colour (SAM Coupé)
- 256-colour (Atari 800 GTIA, AGA)
- 512-colour 9-bit (Atari ST, Mega Drive, MSX2, PC Engine — same colour space)
- 4096-colour 12-bit (Atari STe, Sega Game Gear, Amiga OCS — same colour space)
- 32768-colour 15-bit (SNES, Game Boy Color, GBA — same colour space)

### Import Formats
PNG, BMP, JPEG, WebP, TIFF, GIF (animated→frames), TGA, PCX, DDS, PSD,
IFF ILBM (8-bit/24-bit/HAM6/HAM8/EHB/PackBits — tested on PS2 tools),
Amiga .info (Classic bitplane 2/4/8bp per SDK spec, NewIcon IM1=),
Windows ICO, Apple ICNS, SVG,
ZX SCR, MSX SC2, Atari ST PI1, C64 Koala, C64 Art Studio, ZX Next NXI/PAL

### Export Formats
PNG, BMP, TGA, DDS (BGRA8), PCX, IFF ILBM, IFF HAM,
ZX SCR, ZX TAP, ZX Next NXI/NEX/PAL,
MSX SC2/COM, Atari ST PI1, C64 PRG, C64M PRG, Plus/4 PRG, VIC-20 PRG,
Windows ICO (multi-size), Apple ICNS (multi-size PNG bundle),
Amiga .info (any size, correct DiskObject structure), SVG

### Batch Convert
**File → Batch Convert → Icons:** .info ↔ ICO ↔ ICNS ↔ PNG ↔ TGA ↔ SVG  
**File → Batch Convert → Textures:** PNG/BMP/TGA/DDS/PCX/TIFF with optional resize + power-of-two snap

### Snap to Palette (Load button or File menu)
- Open + snap to palette (hard snap)
- Open + snap to palette (dithered) — Floyd-Steinberg / Bayer 4×4 / Checkerboard
- Open + snap to pal, canvas size (resize then snap)
- Open + snap to pal, canvas size (dither)

### Render As (Picture menu)
ASCII art, ANSI block art, PETSCII (C64 2×2 quad blocks), Teletext mosaic (8col)

### Animation
Frame timeline strip, thumbnails, play/stop, onion skin overlay,
GIF import (all frames), GIF export (animated), PNG sequence export

### View Tools
- Colour clash visualiser — red overlay on ZX Spectrum/C64 attribute violations
- Character/Font Editor — 8×8 or 8×16 bit grid, 128 chars, binary/C/ASM export
- Sprite Editor — slice canvas into frames, platform presets, zoom, export sheet

### Canvas Modes
Platform (retro constraints), Texture (power-of-two), Icon (standard sizes), Free

---

## Repositories
- **Main:** https://github.com/X-Seti/Img-Factory-1.6
- **Standalone:** https://github.com/X-Seti/Deluxe-Paint-Clone---Img-Factory

## TODO
See `TODO.md` for planned features including layers, gradient fill, magic wand,
history panel, rulers, guides, tile map editor, KDE6 .info thumbnail plugin.
