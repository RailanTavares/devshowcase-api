from typing import List

from sqlalchemy.orm import Session, joinedload

from app.crud.technology import get_technologies_by_ids
from app.models.project import Project
from app.schemas.project import ProjectCreate


def create_project(db: Session, data: ProjectCreate) -> Project:
    technologies = get_technologies_by_ids(db, data.technology_ids)

    project = Project(
        title=data.title,
        description=data.description,
        repository_url=str(data.repository_url),
        demo_url=str(data.demo_url) if data.demo_url else None,
        profile_id=data.profile_id,
        technologies=technologies,
    )
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


def get_all_projects(db: Session) -> List[Project]:
    return (
        db.query(Project)
        .options(joinedload(Project.technologies))
        .all()
    )


def get_project_by_id(db: Session, project_id: int) -> Project:
    return (
        db.query(Project)
        .options(joinedload(Project.technologies))
        .filter(Project.id == project_id)
        .first()
    )
