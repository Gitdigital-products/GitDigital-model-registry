from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field

class ModelMetadata(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    version: str  # e.g., "v1.0.4"
    framework: str # e.g., "PyTorch", "TensorFlow", "ONNX"
    stage: str = "Development" # Development, Staging, Production, Archived
    s3_path: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
