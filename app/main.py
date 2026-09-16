from fastapi import FastAPI

from app.database import Base, engine
from app import models  # noqa: F401 - garante que todos os models sejam registrados
from app.routers import profiles, technologies, projects

# Cria as tabelas no banco de dados (caso ainda não existam)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="DevShowcase API",
    description="API para cadastro de perfis de desenvolvedores, seus projetos, "
    "tecnologias utilizadas e feedbacks recebidos.",
    version="1.0.0",
)

app.include_router(profiles.router)
app.include_router(technologies.router)
app.include_router(projects.router)


@app.get("/", tags=["Health"])
def root():
    """Endpoint simples para checar se a API está no ar."""
    return {"status": "ok", "message": "DevShowcase API está no ar 🚀"}
