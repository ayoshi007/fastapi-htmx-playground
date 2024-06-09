import pathlib
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.models.game import GameInfo

PROJECT_BASE_DIR = pathlib.Path(__file__).parent
STATIC_FILE_DIR = PROJECT_BASE_DIR / "static"
TEMPLATE_DIR = PROJECT_BASE_DIR / "templates"
app = FastAPI(
    title="Graphical App Catalogue",
)
templates = Jinja2Templates(directory=TEMPLATE_DIR)

app.mount(path="/static", app=StaticFiles(directory=STATIC_FILE_DIR), name="static")

games = {
    f"game{i}": GameInfo(name=f"game{i}", description=f"description{i}")
    for i in range(10)
}


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(request, name="index.html", context={
        "title": app.title,
    })


@app.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request, name="home.html", context={
        "games": games,
    })


@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse(request, name="about.html")


@app.get("/game/{name}", response_class=HTMLResponse)
async def game_page(request: Request, name: str):
    return templates.TemplateResponse(request, name="game.html", context={
        "game": games[name],
    })
