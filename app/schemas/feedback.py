from pydantic import BaseModel, Field, ConfigDict


class FeedbackCreate(BaseModel):
    """DTO de entrada para cadastro de feedback em um projeto."""

    author_name: str = Field(..., min_length=1, max_length=150)
    comment: str = Field(..., min_length=1, max_length=1000)
    rating: int = Field(..., ge=1, le=5, description="Nota de 1 a 5")
    # project_id será pegue pela rota, não precisa no corpo (ou se mantido, pode ser sobrescrito)


class FeedbackOut(BaseModel):
    """DTO de saída para feedback."""

    id: int
    author_name: str
    comment: str
    rating: int
    project_id: int

    model_config = ConfigDict(from_attributes=True)
