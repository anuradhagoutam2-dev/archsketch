# ArchSketch

Privacy-first architecture diagramming for enterprise architects.

**One HTML file. No install. No login. No data stored. Open it and draw.**

[Try it live](https://anuradhabose.github.io/archsketch) · [Download index.html](https://raw.githubusercontent.com/anuradhabose/archsketch/main/index.html)

---

## The Founding Principle

An architect should be able to diagram the most sensitive enterprise topology without anything leaving their machine. ArchSketch enforces this by design — it is a single HTML file that runs entirely in the browser. There is no server, no account, no telemetry, no cookies. When you close the tab, everything is gone.

---

## Features

- Architecture diagrams with typed components (device, service, database, queue, cloud, actor)
- UML and Mermaid diagram support via `diagramtype|` switching — sequence, class, state, flowchart, ER, Gantt, mindmap, and more
- Live preview as you type
- Strict but helpful validation — typos get suggestions, not just errors
- Export to SVG, PNG, Markdown, and standalone HTML
- Import from `.md` files containing an archsketch code block
- Dark editor, white preview, resizable split pane
- MIT licensed, free forever

---

## Quickstart

Download `index.html` and open it in any browser. That is all.

```
curl -O https://raw.githubusercontent.com/anuradhabose/archsketch/main/index.html
open index.html
```

Or clone the repo and open the file directly — no build step, no `npm install`, no server required.

---

## Syntax

### Components

```archsketch
device [edge router] color sky-blue font calibri bold
service [api gateway] color teal font verdana italic
database [config db] color dark-blue
queue [event bus] color yellow
cloud [dashboard] color mint
actor [end user] color light-purple
```

### Connections

```archsketch
edge router -> api gateway : https
api gateway --> config db : dashed line
a -> b -> c : chained
```

### Groups

```archsketch
group [backend zone] color light-grey
  service [api gateway]
  database [config db]
end
```

### UML and Mermaid diagrams

Start your file with a `diagramtype|` declaration. The rest is native Mermaid syntax.

```archsketch
diagramtype|sequence
participant User
participant API
User->>API: POST /login
API-->>User: JWT token
```

Supported types: `sequence` `class` `state` `activity` `usecase` `component` `deployment` `flowchart` `er` `gantt` `mindmap` `timing`

---

## Colour Palette

All colour names are lowercase. Three variants available for each: base, `light-x`, `dark-x`.

`red` `blue` `green` `teal` `yellow` `mustard` `grey` `sky-blue` `cyan` `purple` `coral` `mint` `lavender` `peach` `slate` `white` `black`

---

## Validation Rules

- Everything must be lowercase
- Spelling sensitive — typos show an error with a suggestion (`"reed" is not a valid colour. try: red`)
- Validation only applies in architecture mode, not UML/Mermaid mode

---

## Export Formats

| Format | Use case |
|--------|----------|
| SVG | Vector, scalable, embeds cleanly in docs |
| PNG | 2x resolution for presentations and emails |
| Markdown | Source code wrapped in an archsketch code block, shareable in repos |
| HTML | Standalone file with diagram and source embedded — no dependencies |

---

## Import

Export your diagram as Markdown and re-import it later via the Open button. The tool reads the archsketch code block and restores your diagram. Nothing is cached or remembered between sessions.

---

## Optional Backend

A minimal Python/FastAPI backend is included in `backend/` for teams that want to add `.md` file parsing via API. It is stateless — it processes the upload in memory and returns the extracted code. Nothing is written to disk.

See [backend/README.md](backend/README.md) for setup instructions.

---

## Contributing

Pull requests are welcome. Before submitting, check your change against the founding principles:

1. Does it require a server call by default? If yes, do not add it.
2. Does it require install steps or a build tool? If yes, do not add it.
3. Is it behind any kind of paywall or flag? If yes, do not add it.
4. Does every error message suggest a fix? It should.

---

## License

MIT. Free forever. No exceptions.
