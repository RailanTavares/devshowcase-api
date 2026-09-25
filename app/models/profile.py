from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

from app.database import Base


class Profile(Base):
    """Perfil do Desenvolvedor. Relacionamento: Profile 1 : N Project."""

    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(150), nullable=False)
    email = Column(String(150), nullable=False, unique=True, index=True)
    bio = Column(Text, nullable=True)
    github_url = Column(String(300), nullable=True)
    avatar_url = Column(String(300), nullable=True)

    # Um perfil possui vários projetos
    projects = relationship(
        "Project",
        back_populates="profile",
        cascade="all, delete-orphan",
    )
