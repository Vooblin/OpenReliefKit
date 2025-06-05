from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Resource Tracker"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
