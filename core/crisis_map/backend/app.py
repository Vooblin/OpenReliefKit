from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Crisis Map API"}


@app.get("/ui", response_class=HTMLResponse)
def get_ui():
    with open("/app/frontend/index.html") as f:
        return f.read()
