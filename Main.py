from fastapi import FastAPI
from routes import register, list_models, metadata

app = FastAPI(title="GitDigital Model Registry")

app.include_router(register.router, prefix="/register")
app.include_router(list_models.router, prefix="/list")
app.include_router(metadata.router, prefix="/metadata")

@app.get("/")
def root():
    return {"status": "model registry online"}
