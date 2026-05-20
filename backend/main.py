import re
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="ArchSketch API",
    description="Stateless backend for ArchSketch. Processes .md uploads and returns diagram code. Stores nothing.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

VALID_UML_TYPES = {
    "sequence", "class", "state", "activity", "usecase",
    "component", "deployment", "flowchart", "er", "gantt", "mindmap", "timing",
}


class ParsedDiagram(BaseModel):
    code: str
    diagram_type: str


@app.post("/upload", response_model=ParsedDiagram)
async def upload_md(file: UploadFile = File(...)):
    if not (file.filename or "").endswith(".md"):
        raise HTTPException(status_code=400, detail="only .md files are accepted")

    raw = await file.read()
    try:
        content = raw.decode("utf-8")
    except UnicodeDecodeError:
        raise HTTPException(status_code=400, detail="file must be utf-8 encoded")

    match = re.search(r"```archsketch\n(.*?)\n```", content, re.DOTALL)
    if not match:
        raise HTTPException(status_code=422, detail="no archsketch code block found in the file")

    code = match.group(1).strip()

    first_line = code.split("\n")[0].strip()
    type_match = re.match(r"^diagramtype\|(.+)$", first_line)
    if type_match:
        diagram_type = type_match.group(1).strip().lower()
        if diagram_type not in VALID_UML_TYPES:
            raise HTTPException(
                status_code=422,
                detail=f"unknown diagram type '{diagram_type}' in file",
            )
    else:
        diagram_type = "architecture"

    return ParsedDiagram(code=code, diagram_type=diagram_type)


@app.get("/health")
def health():
    return {"status": "ok"}
