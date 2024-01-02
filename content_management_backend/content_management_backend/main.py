import uvicorn
from assistant_commons.example_lib import a
from fastapi import FastAPI

print(a)


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("content_management_backend.main:app", host="0.0.0.0", port=8000, reload=True)
