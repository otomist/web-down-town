# uvicorn server:app --port=8000 --reload --log-level debug
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from discord_auth import router as discord_router

app = FastAPI()
app.include_router(discord_router)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/load_content", response_class=HTMLResponse)
async def load_content(request: Request):
    return templates.TemplateResponse("partial.html", {"request": request})
