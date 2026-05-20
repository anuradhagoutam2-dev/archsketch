# ArchSketch Backend

Optional. Stateless. Stores nothing.

This backend exists solely to parse `.md` files uploaded by the user and return the extracted archsketch code block as JSON. It holds no state, writes nothing to disk, and has no database.

## Setup

```bash
cd backend

# create and activate virtual environment
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

API docs available at `http://localhost:8000/docs` once running.

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| POST | `/upload` | Upload a `.md` file, returns `{code, diagram_type}` |
| GET | `/health` | Liveness check |

## Privacy

The uploaded file is read into memory, parsed, and discarded. Nothing is logged, stored, or transmitted. The backend is an opt-in convenience for teams that prefer server-assisted parsing — the frontend works fully without it using the browser File API.
