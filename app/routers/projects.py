from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud import profile as profile_crud
from app.crud import project as project_crud
from app.database import get_db
from app.schemas.project import ProjectCreate, ProjectOut

router = APIRouter(prefix="/api/projects", tags=["Projects"])


@router.post("", response_model=ProjectOut, status_code=status.HTTP_201_CREATED)
def create_project(data: ProjectCreate, db: Session = Depends(get_db)):
    """Cadastra um novo projeto, vinculado a um perfil e a tecnologias existentes."""
    profile = profile_crud.get_profile_by_id(db, data.profile_id)
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Perfil com id {data.profile_id} não encontrado. Cadastre o perfil antes do projeto.",
        )
    return project_crud.create_project(db, data)


@router.get("", response_model=List[ProjectOut])
def list_projects(db: Session = Depends(get_db)):
    """Lista todos os projetos cadastrados."""
    return project_crud.get_all_projects(db)
