"""
Script de seed: popula o banco de dados com dados de exemplo, direto pelas
classes do SQLAlchemy (não precisa do servidor rodando).

Uso:
    python scripts/seed_data.py            # popula se o banco estiver vazio
    python scripts/seed_data.py --force     # apaga tudo e recria os dados
"""
import os
import sys

# Garante que o pacote "app" seja encontrado quando o script roda da raiz do projeto
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app.database import Base, SessionLocal, engine  # noqa: E402
from app.models.feedback import Feedback  # noqa: E402
from app.models.profile import Profile  # noqa: E402
from app.models.project import Project  # noqa: E402
from app.models.technology import Technology  # noqa: E402

FORCE = "--force" in sys.argv


def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        if FORCE:
            print("Apagando dados existentes...")
            db.query(Feedback).delete()
            db.execute(Project.__table__.delete())
            db.query(Technology).delete()
            db.query(Profile).delete()
            db.commit()

        if db.query(Profile).count() > 0:
            print("O banco já contém dados. Use --force para recriar do zero.")
            return

        print("Criando perfil de exemplo...")
        profile = Profile(
            full_name="Ana Souza",
            email="ana.souza@email.com",
            bio="Desenvolvedora fullstack, apaixonada por criar APIs bem estruturadas.",
            github_url="https://github.com/anasouza",
            avatar_url="https://example.com/avatar-ana.png",
        )
        db.add(profile)
        db.commit()
        db.refresh(profile)

        print("Criando tecnologias de exemplo...")
        tech_names = ["Python", "FastAPI", "PostgreSQL", "React"]
        technologies = [Technology(name=name) for name in tech_names]
        db.add_all(technologies)
        db.commit()
        for tech in technologies:
            db.refresh(tech)

        print("Criando projeto de exemplo...")
        project = Project(
            title="DevShowcase API",
            description="Backend da plataforma DevShowcase, construído com FastAPI.",
            repository_url="https://github.com/anasouza/devshowcase-api",
            demo_url="https://devshowcase-demo.com",
            profile_id=profile.id,
            technologies=technologies[:3],  # Python, FastAPI, PostgreSQL
        )
        db.add(project)
        db.commit()
        db.refresh(project)

        print("Criando feedback de exemplo...")
        feedback = Feedback(
            author_name="João Pereira",
            comment="Projeto muito bem estruturado, parabéns pela organização do código!",
            rating=5,
            project_id=project.id,
        )
        db.add(feedback)
        db.commit()

        print("\nSeed concluído com sucesso:")
        print(f"  - Profile id={profile.id} ({profile.full_name})")
        print(f"  - Technologies: {[t.id for t in technologies]} {tech_names}")
        print(f"  - Project id={project.id} ({project.title})")
        print(f"  - Feedback id={feedback.id}")
        print("\nUse esses IDs no Postman durante a gravação, se quiser pular a criação manual.")

    finally:
        db.close()


if __name__ == "__main__":
    seed()
