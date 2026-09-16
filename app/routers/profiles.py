from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud import profile as profile_crud
from app.database import get_db
from app.schemas.profile import ProfileCreate, ProfileWithProjectsOut

router = APIRouter(prefix="/api/profiles", tags=["Profiles"])


@router.post("", response_model=ProfileWithProjectsOut, status_code=status.HTTP_201_CREATED)
def create_profile(data: ProfileCreate, db: Session = Depends(get_db)):
    """Cadastra um novo perfil de desenvolvedor."""
    existing = profile_crud.get_profile_by_email(db, data.email)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Já existe um perfil cadastrado com este e-mail.",
        )
    return profile_crud.create_profile(db, data)


@router.get("/{profile_id}", response_model=ProfileWithProjectsOut)
def get_profile(profile_id: int, db: Session = Depends(get_db)):
    """Busca um perfil pelo ID."""
    profile = profile_crud.get_profile_by_id(db, profile_id)
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Perfil com id {profile_id} não encontrado.",
        )
    return profile
