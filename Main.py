from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import Session, SQLModel, create_engine, select
from typing import List
from models import ModelMetadata  # Importing the schema we defined earlier

# Database Setup
sqlite_url = "sqlite:///./registry.db"
engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

app = FastAPI(title="GitDigital Model Registry")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# --- Endpoints ---

@app.post("/models/", response_model=ModelMetadata)
def register_model(model: ModelMetadata, session: Session = Depends(get_session)):
    """Registers a new model version and its S3 location."""
    session.add(model)
    session.commit()
    session.refresh(model)
    return model

@app.get("/models/{name}", response_model=List[ModelMetadata])
def get_model_history(name: str, session: Session = Depends(get_session)):
    """Retrieves all versions of a specific model by name."""
    statement = select(ModelMetadata).where(ModelMetadata.name == name)
    results = session.exec(statement).all()
    if not results:
        raise HTTPException(status_code=404, detail="Model not found")
    return results

@app.patch("/models/{model_id}/promote")
def promote_model(model_id: int, target_stage: str, session: Session = Depends(get_session)):
    """Promotes a model (e.g., from 'Staging' to 'Production')."""
    db_model = session.get(ModelMetadata, model_id)
    if not db_model:
        raise HTTPException(status_code=404, detail="Model ID not found")
    
    db_model.stage = target_stage
    session.add(db_model)
    session.commit()
    session.refresh(db_model)
    return {"message": f"Model {db_model.name} promoted to {target_stage}"}
