# uvicorn server:app --port=8111 --reload --log-level debug
print("hello web")

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "<h1>Hello World</h1>"
