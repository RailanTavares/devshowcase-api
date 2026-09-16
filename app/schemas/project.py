from typing import List, Optional

from pydantic import BaseModel, Field, HttpUrl, ConfigDict, field_validator

from app.schemas.technology import TechnologyOut


class ProjectCreate(BaseModel):
    """DTO de entrada para cadastro de projeto."""

    title: str = Field(..., min_length=1, max_length=150, description="Título do projeto (não pode ser vazio)")
    description: Optional[str] = Field(None, max_length=2000)
    repository_url: HttpUrl = Field(..., description="URL válida do repositório do projeto")
    demo_url: Optional[HttpUrl] = Field(None, description="URL válida da demo/deploy do projeto")
    profile_id: int = Field(..., gt=0, description="ID do perfil (desenvolvedor) dono do projeto")
    technology_ids: List[int] = Field(default_factory=list, description="IDs das tecnologias usadas no projeto")

    @field_validator("title")
    @classmethod
    def title_must_not_be_blank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("O título não pode ser vazio ou conter apenas espaços.")
        return value.strip()


class ProjectSummaryOut(BaseModel):
    """DTO de saída resumido, usado dentro de ProfileWithProjectsOut."""

    id: int
    title: str
    repository_url: str

    model_config = ConfigDict(from_attributes=True)


class ProjectOut(BaseModel):
    """DTO de saída completo para projeto."""

    id: int
    title: str
    description: Optional[str] = None
    repository_url: str
    demo_url: Optional[str] = None
    profile_id: int
    technologies: List[TechnologyOut] = []

    model_config = ConfigDict(from_attributes=True)
