from typing import Optional

from sqlalchemy.orm import Session

from app.models.profile import Profile
from app.schemas.profile import ProfileCreate


def create_profile(db: Session, data: ProfileCreate) -> Profile:
    profile = Profile(
        full_name=data.full_name,
        email=data.email,
        bio=data.bio,
        github_url=str(data.github_url) if data.github_url else None,
        avatar_url=str(data.avatar_url) if data.avatar_url else None,
    )
    db.add(profile)
    db.commit()
    db.refresh(profile)
    return profile


def get_profile_by_id(db: Session, profile_id: int) -> Optional[Profile]:
    return db.query(Profile).filter(Profile.id == profile_id).first()


def get_profile_by_email(db: Session, email: str) -> Optional[Profile]:
    return db.query(Profile).filter(Profile.email == email).first()
