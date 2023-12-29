from assistant_commons.example_lib import a
from fastapi import FastAPI

print(a)


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}