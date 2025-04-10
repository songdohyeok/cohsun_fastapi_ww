from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return "Hello FastAPI"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8000)