<<<<<<< HEAD
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, status, Query
=======
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
>>>>>>> 2e8eda9a8d67dc8a2cbc43f1b17f27ba98712a70
from sqlalchemy.orm import Session

from app.crud import profile as profile_crud
from app.crud import project as project_crud
<<<<<<< HEAD
from app.crud import feedback as feedback_crud
from app.database import get_db
from app.schemas.project import ProjectCreate, ProjectOut
from app.schemas.feedback import FeedbackCreate, FeedbackOut
=======
from app.database import get_db
from app.schemas.project import ProjectCreate, ProjectOut
>>>>>>> 2e8eda9a8d67dc8a2cbc43f1b17f27ba98712a70

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
<<<<<<< HEAD
def list_projects(
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0, description="Pular N registros (paginação)"),
    limit: int = Query(10, ge=1, le=100, description="Quantidade de registros a retornar"),
    technology: Optional[int] = Query(None, description="Filtrar projetos pelo ID da tecnologia")
):
    """Lista todos os projetos cadastrados."""
    return project_crud.get_all_projects(db, skip=skip, limit=limit, technology_id=technology)


@router.post("/{id}/feedbacks", response_model=FeedbackOut, status_code=status.HTTP_201_CREATED)
def create_project_feedback(id: int, data: FeedbackCreate, db: Session = Depends(get_db)):
    """Cadastra feedback (nota e comentário) e atualiza a média do projeto."""
    project = project_crud.get_project_by_id(db, id)
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Projeto não encontrado.")
    return feedback_crud.create_feedback(db, project_id=id, data=data)


@router.put("/{id}/upvote", response_model=ProjectOut)
def upvote_project(id: int, db: Session = Depends(get_db)):
    """Adiciona um voto/curtida ao projeto."""
    project = project_crud.get_project_by_id(db, id)
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Projeto não encontrado.")
    
    project.upvotes += 1
    db.commit()
    db.refresh(project)
    return project
=======
def list_projects(db: Session = Depends(get_db)):
    """Lista todos os projetos cadastrados."""
    return project_crud.get_all_projects(db)
>>>>>>> 2e8eda9a8d67dc8a2cbc43f1b17f27ba98712a70
