from pydantic import BaseModel, Field, ConfigDict


class TechnologyCreate(BaseModel):
    """DTO de entrada para cadastro de tecnologia."""

    name: str = Field(..., min_length=1, max_length=100, description="Nome da tecnologia, ex: Python")


class TechnologyOut(BaseModel):
    """DTO de saída para tecnologia."""

    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)
