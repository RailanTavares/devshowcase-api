from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.technology import Technology
from app.schemas.technology import TechnologyCreate


def create_technology(db: Session, data: TechnologyCreate) -> Technology:
    technology = Technology(name=data.name.strip())
    db.add(technology)
    db.commit()
    db.refresh(technology)
    return technology


def get_technology_by_name(db: Session, name: str) -> Optional[Technology]:
    return db.query(Technology).filter(Technology.name == name.strip()).first()


def get_all_technologies(db: Session) -> List[Technology]:
    return db.query(Technology).all()


def get_technologies_by_ids(db: Session, ids: List[int]) -> List[Technology]:
    if not ids:
        return []
    return db.query(Technology).filter(Technology.id.in_(ids)).all()
