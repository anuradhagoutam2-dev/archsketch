# ArchSketch — Feature Reference

**Version:** v1.0  
**Live:** https://archsketch-app.github.io  
**Last updated:** 2026-05-21

---

## Core Principle

Single HTML file. No install. No login. No data stored. Open it and draw. Everything runs in the browser — nothing ever leaves the machine.

---

## Diagram Types

### Block Diagram (default tab)
Custom ArchSketch syntax for architecture diagrams.

**Component types:**
| Keyword | Shape |
|---------|-------|
| `device` | rounded rectangle |
| `service` | rectangle |
| `database` | cylinder |
| `queue` | parallelogram |
| `cloud` | cloud shape |
| `actor` | person / stick figure |

**Syntax:**
```
device [edge router] color sky-blue font calibri bold
service [api gateway] color teal
database [config db] color dark-blue
queue [event bus] color yellow
cloud [dashboard] color mint
actor [end user] color light-purple
```

**Connections:**
```
edge router -> api gateway : https
api gateway --> config db : dashed line
a -> b -> c : chained
```

**Groups:**
```
group [backend zone] color light-grey
  service [api gateway]
  database [config db]
end
```

**Validation:** Live, strict but helpful — typos show a suggestion (`"reed" is not a valid colour. try: red`). Everything must be lowercase.

---

### UML / Mermaid Diagram Types
All 12 types activated with a `diagramtype|` declaration. The rest is native Mermaid syntax.

| Tab | Type | diagramtype declaration |
|-----|------|------------------------|
| sequence | Sequence diagram | `diagramtype|sequence` |
| class | Class diagram | `diagramtype|class` |
| state | State machine | `diagramtype|state` |
| activity | Activity / flowchart | `diagramtype|activity` |
| usecase | Use case | `diagramtype|usecase` |
| component | Component | `diagramtype|component` |
| deployment | Deployment | `diagramtype|deployment` |
| flowchart | Flowchart | `diagramtype|flowchart` |
| er | Entity relationship | `diagramtype|er` |
| gantt | Gantt chart | `diagramtype|gantt` |
| mindmap | Mind map | `diagramtype|mindmap` |
| timing | Roadmap (custom renderer) | `diagramtype|timing` |

---

## Sequence Diagram — Extended Features

### Participant types
```
participant Customer       // box
actor ExternalBank         // stick figure / oval
```

### Arrow types
```
A->>B: solid arrow
A-->>B: dashed arrow (response)
A->B: solid open arrow
A-->B: dashed open arrow
A->>+B: activate lifebar
B-->>-A: deactivate lifebar
```

### Blocks
```
alt condition              // conditional — first branch
    ...
else other condition
    ...
end

loop Label                 // repeat
    ...
end

opt optional               // optional block
    ...
end

par label                  // parallel
    ...
and
    ...
end

rect rgb(200,200,200)      // background box (no nesting alt inside)
    ...
end
```

### Notes
```
note over A,B: text
note right of A: text
note left of A: text
```

### Create and Destroy
```
create participant Worker
A->>Worker: assign task
destroy Worker
A->>Worker: release         // destroy must come BEFORE the last message to that participant
```

### Autonumber (toolbar buttons — sequence tab only)

| Button | Behaviour |
|--------|-----------|
| off | No numbers (default) |
| 1 2 3 | Sequential integers via Mermaid autonumber |
| 1a 1b | Hierarchical — numbers at top level, letters inside blocks |
| from N | Shifts the start number (works with both modes) |

**Hierarchical numbering scheme:**
- Top level: `1`, `2`, `3`
- Inside any block (alt/loop/par/opt): `1a`, `1b`, `1c`
- Prefix carries from parent: entering a block after arrow `2` gives `2a`, `2b`
- `else` and `and` continue the same block counter without reset

**Jump syntax — skip steps conditionally:**
```
%% #5
```
Placed on its own line, jumps the counter so the next arrow at this depth is labelled 5 (or the 5th letter inside a block). Use inside `alt/else` branches to skip step numbers on a conditional path.

---

## Flowchart — Direction Toggle
When on the flowchart tab, two buttons appear in the preview header:
- **↓ top-bottom** — `flowchart TD`
- **→ left-right** — `flowchart LR`

---

## Toolbar Actions

| Button | Action |
|--------|--------|
| ↓ svg | Download diagram as scalable vector (SVG) |
| ↓ png | Download diagram as 2× raster image (PNG) |
| ↓ md | Download source as Markdown with archsketch code block |
| ↓ html | Download as standalone HTML — diagram + source, no dependencies |
| ^ open | Open an existing `.md` or `.html` file to re-import a diagram |
| ⬡ example | Load a full real-life example for the current diagram type |
| ✕ clear | Clear the editor (with confirmation) |
| ? syntax guide | Open the in-app syntax reference |

---

## Import / Re-import

- **Open `.md`**: reads the `archsketch` code block from a previously downloaded markdown file
- **Open `.html`**: reads the source from a previously downloaded standalone HTML file
- Round-trip safe: download as `.md` → edit → re-open → diagram restores exactly

---

## Colour Palette

All colour names are lowercase. Three variants for each: base, `light-x`, `dark-x`.

`red` `blue` `green` `teal` `yellow` `mustard` `grey` `sky-blue` `cyan` `purple` `coral` `mint` `lavender` `peach` `slate` `white` `black`

---

## Zoom Controls
- **−** / **+** buttons: zoom out / in by 15% per click
- **reset**: return to 100%
- Available for all diagram types

---

## Preview Panel
- Live render as you type (300 ms debounce)
- Mode badge shows current diagram type
- Error displayed inline in preview — exact Mermaid error message shown in red monospace
- Diagram info shown (node count, connection count for block diagrams)

---

## Status Bar
- Lines count
- Node count (block diagram mode)
- Error count — `✓ no errors` or `⚠ N error(s)` with red background
- Privacy reminder: `everything lowercase · spelling sensitive · no data stored`

---

## Export Formats

| Format | Use case |
|--------|----------|
| SVG | Vector — embeds in wikis, docs, presentations without blur |
| PNG | 2× raster — emails, slide decks, reports |
| Markdown | Source code in archsketch code block — commit to repo, re-import later |
| HTML | Standalone page with diagram and source — share with anyone, no install needed |

---

## Optional Backend
Minimal Python / FastAPI backend in `backend/` for teams that want `.md` file parsing via API.
- Stateless — processes in memory, returns extracted code, writes nothing to disk
- Endpoints: `POST /upload`, `GET /health`
- Not required — frontend works fully without it

---

## Privacy & Security
- No login, no account, no cookies
- No network calls except loading Mermaid.js from CDN on first load
- No telemetry, no analytics
- Closing the tab discards everything
- Downloaded HTML files have no external dependencies after export

---

## Tech Stack
- Single HTML file — no build tools, no npm, no server required
- Mermaid.js v10.9.6 (CDN) for UML rendering
- Custom parser and renderer for block diagrams
- Custom roadmap renderer for timing/timeline type (bypasses Mermaid timeline)
- MIT licensed, open source
