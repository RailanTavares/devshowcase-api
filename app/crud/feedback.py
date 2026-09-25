from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.feedback import Feedback
from app.models.project import Project
from app.schemas.feedback import FeedbackCreate

def create_feedback(db: Session, project_id: int, data: FeedbackCreate) -> Feedback:
    # Cria o feedback
    feedback = Feedback(
        author_name=data.author_name,
        comment=data.comment,
        rating=data.rating,
        project_id=project_id,
    )
    db.add(feedback)
    
    # Atualiza a nota média do projeto
    project = db.query(Project).filter(Project.id == project_id).first()
    if project:
        # Calcula nova média
        # Como o feedback ainda não foi comitado, precisamos somar ele na mão 
        # ou comitar primeiro. Melhor comitar o feedback primeiro.
        db.commit()
        db.refresh(feedback)
        
        avg_rating = db.query(func.avg(Feedback.rating)).filter(Feedback.project_id == project_id).scalar()
        project.average_rating = float(avg_rating) if avg_rating else 0.0
        db.commit()
        db.refresh(project)
        
    return feedback
