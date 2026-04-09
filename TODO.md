# DP5 Workshop — TODO & Roadmap

Items marked ✅ are complete.

---

## Core Drawing Tools

- [ ] **Brush shapes** — square, diagonal, custom shape; brush shape library
- [ ] **Brush pressure simulation** — vary opacity based on mouse speed
- [ ] **Dotted / dashed line tool** — configurable dash pattern
- [ ] **Perspective grid overlay** — 1/2/3-point perspective for assisted drawing

---

## Selection Improvements

- [ ] **Magic wand** — select by colour tolerance
- [ ] **Grow / shrink selection** — expand or contract by N pixels
- [ ] **Feather selection edges**
- [ ] **Invert selection**
- [ ] **Select by colour range**

---

## Layer / Object System

- [ ] **Named layers** with visibility toggle and opacity slider
- [ ] **Layer blend modes** — Multiply, Screen, Overlay, Add, Difference
- [ ] **Flatten to canvas**
- [ ] **Layer reorder** — drag to change stacking order
- [ ] **Non-destructive objects** — moveable until committed

---

## Colour Tools

- [ ] **HSV colour wheel picker** — inline wheel replacing QColorDialog
- [ ] **Gradient tool** — linear and radial FG→BG fill
- [ ] **Replace colour** — swap one colour for another canvas-wide
- [ ] **Colour count / histogram**
- [ ] **Palette lock mode** — restrict drawing to active palette colours (true Amiga mode)

---

## Filters & Effects

- [ ] **Blur / Sharpen** — 3×3 convolution
- [ ] **Pixelate** — reduce to coarser grid
- [ ] **Edge detect** — Sobel / Laplacian
- [ ] **Emboss / Relief**
- [ ] **Colour quantise to palette** — snap pixels to nearest palette colour

---

## Canvas & View

- [ ] **Reference image panel** — non-editable overlay at adjustable opacity (for tracing)
- [ ] **Tile preview** — 3×3 tiled view (essential for GTA textures)
- [ ] **Before/after split view**
- [ ] **Rulers and guides** — drag from ruler; snap to guides
- [ ] **Canvas background colour** — configurable checkerboard or solid for transparent areas

---

## Animation

- [ ] **Animation frames** — flip-book navigation (original DP5 feature)
- [ ] **Export as GIF**
- [ ] **Export as PNG sequence**
- [ ] **Onion skin** — previous/next frame at reduced opacity

---

## Workflow & UX

- [ ] **Project file format (.dp5)** — canvas + palette + layers + brushes in one file
- [ ] **Recent files list** — last 10 opened files
- [ ] **Macro recording** — record and replay tool sequences
- [ ] **Export presets** — named export settings
- [ ] **Canvas notes layer** — non-destructive text annotations

---

## IMG Factory Integration

- [ ] **Direct export to TXD** — send canvas to TXD Workshop as new/replacement texture
- [ ] **Read palette from TXD** — extract TXD palette into user palette
- [ ] **Sprite sheet splitter** — split canvas into tiles, save as IMG entries
- [ ] **COL visualiser overlay** — COL collision mesh semi-transparent over image

---

## Amiga / Retro Specific

- [ ] **HAM mode preview** — simulate Hold-And-Modify artefacts (OCS/ECS)
- [ ] **Bitplane view** — each bitplane as B&W layer (debug IFF)
- [ ] **Copper bar simulator** — horizontal colour-cycling preview
- [ ] **IFF ILBM round-trip verify**

---

## Technical / Infrastructure

- [ ] **Standalone launcher script** — `launch_dp5_workshop.py` in repo root
- [ ] **`.desktop` file** — for Linux app launchers
- [ ] **Wayland app ID** — `QT_WAYLAND_WINDOW_TYPE` for KDE grouping
- [ ] **Unit tests** — canvas ops, flood fill, coordinate transforms
- [ ] **Performance** — offload rendering for canvases > 1024×1024

---

## Completed ✅

- ✅ Full tool set: pencil, eraser, fill, spray, picker, line, curve, rect, ellipse, triangle, polygon, star, lasso, select, zoom, text, stamp, crop, resize
- ✅ **Dither tool** — cycles checkerboard → Bayer 4×4 → off
- ✅ **Symmetry tool** — cycles H → V → Quad → off
- ✅ **Canvas-wide dither** — Floyd-Steinberg, Bayer 4×4, Checkerboard (Picture menu)
- ✅ Right-click shape buttons to toggle outline ↔ filled
- ✅ Marquee select with lift, move, stamp; arrow-key nudge
- ✅ Brush thumbnail + stamp mode
- ✅ Brush Manager — save/load/delete/import PNG brushes
- ✅ **Custom tool icons** — drop PNG/SVG into `icons/` folder
- ✅ Zoom-to-cursor (Ctrl+scroll)
- ✅ Pixel-perfect integer zoom for small canvases
- ✅ **Platform mode** — cell grid, colour constraints, auto-load palette
- ✅ **Platform presets**: Amiga, C64 hires/multi, ZX Spectrum, ZX Next, MSX1, Amstrad CPC, Atari ST, Plus/4, VIC-20, Sinclair QL
- ✅ **New canvas dialog** — platform presets, bit depth, fill colour
- ✅ **Import formats**: ZX SCR, MSX SC2, Atari ST PI1, C64 Koala, C64 Art Studio, ZX Next NXI, ZX Next PAL
- ✅ **Export formats**: ZX SCR, MSX SC2, Atari ST PI1, C64 Koala, C64 Art Studio, ZX Next NXI, ZX Next PAL, IFF ILBM
- ✅ **Executable exports**: ZX Spectrum TAP, ZX Next NEX, C64 PRG (hires+multi), MSX COM, Plus/4 PRG, VIC-20 PRG
- ✅ Retro palette presets — Amiga OCS/AGA/WB, C64, ZX Spectrum, Amstrad CPC, Atari 800/2600, ULA Plus, MSX1, Atari ST, Plus/4, VIC-20, Sinclair QL
- ✅ **Colour history** — last 12 used colours as swatches
- ✅ **Opacity slider** — brush opacity 0–100%
- ✅ Image palette bit-depth quantize (32b/24b/16b/8b)
- ✅ Image palette hue-sort Group button (asc/desc toggle)
- ✅ Palette cols/rows configurable in Settings
- ✅ **Status bar** — toggleable from View menu and Settings
- ✅ **Menu bar** — topbar or dropdown mode
- ✅ **New button** on toolbar
- ✅ UI font size in Settings
- ✅ Gadget visibility per tool in Settings → Gadgets tab
- ✅ Picture operations: flip, rotate, scale, invert, brighten, darken
- ✅ Undo/redo stack (configurable depth)
- ✅ Docked into IMG Factory 1.6 as a tab
- ✅ TXD Workshop Paint button opens selected texture; writes back on Apply
- ✅ Window/app icon — multi-size for taskbar/alt-tab/dock
- ✅ SVG icons on all toolbar and gadget buttons
- ✅ Adaptive gadget bar columns (3/4/5/6)
