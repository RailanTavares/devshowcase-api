from sqlalchemy import Column, ForeignKey, Integer, String, Table, Text, Float
from sqlalchemy.orm import relationship

from app.database import Base

# Tabela de associação para o relacionamento N:N entre Project e Technology
project_technology = Table(
    "project_technology",
    Base.metadata,
    Column("project_id", Integer, ForeignKey("projects.id"), primary_key=True),
    Column("technology_id", Integer, ForeignKey("technologies.id"), primary_key=True),
)


class Project(Base):
    """Projeto cadastrado por um desenvolvedor.

    Relacionamentos:
      - Profile 1 : N Project (um perfil tem vários projetos)
      - Project N : N Technology (um projeto usa várias tecnologias)
      - Project 1 : N Feedback (um projeto recebe várias opiniões)
    """

    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), nullable=False)
    description = Column(Text, nullable=True)
    repository_url = Column(String(300), nullable=False)
    demo_url = Column(String(300), nullable=True)
    average_rating = Column(Float, default=0.0)
    upvotes = Column(Integer, default=0)

    profile_id = Column(Integer, ForeignKey("profiles.id"), nullable=False)

    # Muitos projetos pertencem a um perfil
    profile = relationship("Profile", back_populates="projects")

    # Um projeto tem várias tecnologias, e uma tecnologia pode estar em vários projetos
    technologies = relationship(
        "Technology",
        secondary=project_technology,
        back_populates="projects",
    )

    # Um projeto tem vários feedbacks
    feedbacks = relationship(
        "Feedback",
        back_populates="project",
        cascade="all, delete-orphan",
    )
