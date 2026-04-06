# DP5 Workshop — TODO & Roadmap

Items marked ✅ are complete. All others are planned or in progress.

---

## Core Drawing Tools

- [ ] **Brush shapes** — square, diagonal, custom shape (not just round); brush shape library
- [ ] **Brush pressure simulation** — vary pixel density / opacity based on mouse speed
- [ ] **Dotted / dashed line tool** — configurable dash pattern
- [ ] **Symmetry mode** — mirror drawing horizontally, vertically, or radially (great for logos and sprites)
- [ ] **Perspective grid overlay** — 1/2/3-point perspective grid for assisted drawing

---

## Selection Improvements

- [ ] **Magic wand** — select by colour tolerance (flood-select instead of flood-fill)
- [ ] **Grow / shrink selection** — expand or contract selection rect by N pixels
- [ ] **Feather selection edges** — blend selection boundary
- [ ] **Invert selection** — select everything outside the current selection
- [ ] **Select by colour range** — select all pixels within a colour tolerance across the canvas

---

## Layer / Object System

- [ ] **Named layers** with visibility toggle and opacity slider
- [ ] **Layer blend modes** — Multiply, Screen, Overlay, Add, Difference
- [ ] **Flatten to canvas** — merge all layers into one
- [ ] **Layer reorder** — drag to change stacking order
- [ ] **Non-destructive objects** — keep pasted regions as moveable objects until committed

---

## Colour Tools

- [ ] **HSV colour wheel picker** — replaces QColorDialog with an inline wheel
- [ ] **Colour history row** — last 16 used colours shown as swatches
- [ ] **Gradient tool** — linear and radial fill between FG and BG colours
- [ ] **Replace colour** — swap one specific colour for another across the whole canvas
- [ ] **Colour count / histogram** — show how many pixels of each colour exist (useful for palette-limited Amiga/CPC work)
- [ ] **Palette lock mode** — restrict all drawing to colours currently in the active palette (true Amiga mode)

---

## Filters & Effects

- [ ] **Blur / Sharpen** — 3×3 convolution kernel
- [ ] **Dither** — error-diffusion (Floyd–Steinberg) or ordered (Bayer) dither to reduce to a palette
- [ ] **Pixelate** — reduce to a coarser grid (useful for creating sprites from photos)
- [ ] **Edge detect** — Sobel / Laplacian kernel
- [ ] **Emboss / Relief** — directional emboss effect
- [ ] **Colour quantise to palette** — snap every pixel to the nearest colour in the active palette

---

## Canvas & View

- [ ] **Reference image panel** — load a second image as a non-editable overlay at adjustable opacity (for tracing)
- [ ] **Tile preview** — show the canvas tiled 3×3 so you can see how it repeats (essential for GTA textures)
- [ ] **Before/after split view** — horizontal or vertical split showing original vs edited
- [ ] **Rulers and guides** — drag guides from ruler edges; snap drawing to guides
- [ ] **Canvas background colour** — configurable checkerboard or solid colour for transparent areas

---

## Animation

- [ ] **Animation frames** — multiple canvas frames, flip-book navigation (DP5 original feature)
- [ ] **Export as GIF** — animated GIF from frame sequence
- [ ] **Export as PNG sequence** — numbered files for each frame
- [ ] **Onion skin** — show previous/next frame at reduced opacity while drawing

---

## Workflow & UX

- [ ] **Project file format (.dp5)** — save canvas + palette + layer stack + brush library in one file
- [ ] **Recent files list** — last 10 opened files in File menu
- [ ] **Macro recording** — record a sequence of tool operations and replay them
- [ ] **Canvas notes layer** — non-destructive text annotations that don't bake into pixels
- [ ] **Export presets** — save export settings (format, palette, dither method) as named presets
- [ ] **Redo stack restore after save** — don't clear redo on non-destructive operations

---

## IMG Factory Integration

- [ ] **Direct export to TXD** — send the canvas straight into TXD Workshop as a new or replacement texture entry
- [ ] **Read palette from TXD** — extract the active TXD's palette and load it as the user palette
- [ ] **Sprite sheet splitter** — divide a canvas into equal tiles and save each as a separate IMG entry
- [ ] **COL visualiser overlay** — show COL collision mesh on top of the image as a semi-transparent layer

---

## Amiga / Retro Specific

- [ ] **HAM mode preview** — simulate Hold-And-Modify colour encoding artefacts (Amiga OCS/ECS)
- [ ] **Overscan presets** — standard Amiga screen sizes: 320×200 NTSC, 320×256 PAL, 640×512 etc.
- [ ] **Bitplane view** — show each individual bitplane as a black-and-white layer (for debugging IFF files)
- [ ] **Copper bar simulator** — preview horizontal colour-cycling effects
- [ ] **IFF ILBM round-trip verify** — load IFF, edit, save IFF, compare palette and pixel data

---

## Technical / Infrastructure

- [ ] **Standalone launcher script** — `launch_dp5_workshop.py` in repo root (matches IMG Factory pattern)
- [ ] **`.desktop` file** — `dp5-workshop.desktop` for Linux app launchers and taskbar icon
- [ ] **Wayland app ID** — set `QT_WAYLAND_WINDOW_TYPE` so KDE groups the window correctly
- [ ] **Unit tests** — canvas pixel ops, flood fill, coordinate transforms, selection clipboard
- [ ] **Performance** — offload canvas rendering to a worker thread for large canvases (>1024×1024)

---

## Completed ✅

- ✅ Full tool set: pencil, eraser, fill, spray, picker, line, curve, rect, ellipse, triangle, polygon, star, lasso, select, zoom, text, stamp
- ✅ Right-click shape buttons to toggle outline ↔ filled
- ✅ Marquee select with lift, move, stamp; arrow-key nudge
- ✅ Brush thumbnail + stamp mode; Ctrl+V enters stamp mode
- ✅ Brush Manager — save/load/delete/import PNG brushes
- ✅ Zoom-to-cursor (Ctrl+scroll anchored to mouse position)
- ✅ Scroll area panning (scrollbars, spacebar+drag, middle-mouse)
- ✅ Retro palette presets (Amiga OCS/AGA/WB, C64, ZX Spectrum, Amstrad CPC, Atari 800/2600, ULA Plus)
- ✅ Image palette auto-extracted from opened file
- ✅ Picture operations: flip, rotate, scale, invert, brighten, darken
- ✅ Undo/redo stack (configurable depth)
- ✅ Docked into IMG Factory 1.6 as a tab
- ✅ TXD Workshop Paint button opens selected texture in DP5 Workshop; writes back on Apply
- ✅ Paint Edit button in IMG Factory right panel
- ✅ Window/app icon for taskbar, alt-tab, and dock
- ✅ SVG icons on all toolbar and gadget buttons
- ✅ Adaptive gadget bar columns (2/3/4 or auto based on icon size)
- ✅ IFF ILBM export
- ✅ Bitmap list panel for multi-image sessions
