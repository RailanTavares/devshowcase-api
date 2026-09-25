from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.database import Base


class Feedback(Base):
    """Opinião/avaliação recebida em um projeto. Relacionamento: Project 1 : N Feedback."""

    __tablename__ = "feedbacks"

    id = Column(Integer, primary_key=True, index=True)
    author_name = Column(String(150), nullable=False)
    comment = Column(Text, nullable=False)
    rating = Column(Integer, nullable=False)  # nota de 1 a 5

    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)

    project = relationship("Project", back_populates="feedbacks")
