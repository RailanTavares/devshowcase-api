from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Technology(Base):
    """Tecnologia (ex: Python, React, Docker). Relacionamento: Project N : N Technology."""

    __tablename__ = "technologies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True, index=True)

    projects = relationship(
        "Project",
        secondary="project_technology",
        back_populates="technologies",
    )
