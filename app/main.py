from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Azure App",
    version="1.0.0",
)


@app.get("/")
def home() -> dict[str, str]:
    return {"message": "FastAPI is running on Azure"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "healthy"}