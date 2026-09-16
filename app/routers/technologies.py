from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud import technology as technology_crud
from app.database import get_db
from app.schemas.technology import TechnologyCreate, TechnologyOut

router = APIRouter(prefix="/api/technologies", tags=["Technologies"])


@router.post("", response_model=TechnologyOut, status_code=status.HTTP_201_CREATED)
def create_technology(data: TechnologyCreate, db: Session = Depends(get_db)):
    """Cadastra uma nova tecnologia."""
    existing = technology_crud.get_technology_by_name(db, data.name)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Essa tecnologia já está cadastrada.",
        )
    return technology_crud.create_technology(db, data)


@router.get("", response_model=List[TechnologyOut])
def list_technologies(db: Session = Depends(get_db)):
    """Lista todas as tecnologias cadastradas."""
    return technology_crud.get_all_technologies(db)
