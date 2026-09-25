from typing import List, Optional

from pydantic import BaseModel, EmailStr, Field, HttpUrl, ConfigDict


class ProfileCreate(BaseModel):
    """DTO de entrada para cadastro de perfil."""

    full_name: str = Field(..., min_length=3, max_length=150, description="Nome completo do desenvolvedor")
    email: EmailStr = Field(..., description="E-mail do desenvolvedor")
    bio: Optional[str] = Field(None, max_length=1000)
    github_url: Optional[HttpUrl] = Field(None, description="URL do perfil no GitHub")
    avatar_url: Optional[HttpUrl] = Field(None, description="URL da foto de perfil")


class ProfileOut(BaseModel):
    """DTO de saída para perfil."""

    id: int
    full_name: str
    email: EmailStr
    bio: Optional[str] = None
    github_url: Optional[str] = None
    avatar_url: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class ProfileWithProjectsOut(ProfileOut):
    """DTO de saída para perfil incluindo a lista resumida de projetos."""

    projects: List["ProjectSummaryOut"] = []


# Import tardio para evitar import circular (Project referencia Profile)
from app.schemas.project import ProjectSummaryOut  # noqa: E402

ProfileWithProjectsOut.model_rebuild()
