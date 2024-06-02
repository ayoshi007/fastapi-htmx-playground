import pathlib
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

PROJECT_BASE_DIR = pathlib.Path(__file__).parent
STATIC_FILE_DIR = PROJECT_BASE_DIR / "static"
TEMPLATE_DIR = PROJECT_BASE_DIR / "templates"
app = FastAPI(
    title="FastAPI and WebGL fun",    
)
app.mount(path="/static", app=StaticFiles(directory=STATIC_FILE_DIR), name="static")
templates = Jinja2Templates(directory=TEMPLATE_DIR)

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(request, name="index.html")

@app.post("/games", response_class=HTMLResponse)
async def games(request: Request):
    return templates.TemplateResponse(request, name="games.html")