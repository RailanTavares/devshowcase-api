from pathlib import Path

from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

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

# Libera CORS (útil para o Postman e para acessos externos). Mesmo assim, o
# painel de testes é servido pela própria API (rota /painel) para evitar
# bloqueios de "Private Network Access" que alguns navegadores aplicam quando
# uma página aberta como file:// tenta chamar http://127.0.0.1.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(profiles.router)
app.include_router(technologies.router)
app.include_router(projects.router)

# Caminho do painel de testes HTML, que fica na raiz do projeto (um nível acima de app/)
TESTER_HTML_PATH = Path(__file__).resolve().parent.parent / "devshowcase-tester.html"


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": True,
            "message": exc.detail,
            "status_code": exc.status_code
        },
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "error": True,
            "message": "Erro de validação nos dados enviados.",
            "details": exc.errors()
        },
    )


@app.get("/painel", include_in_schema=False)
def painel():
    """Serve o painel de testes visual na mesma origem da API (evita bloqueio de CORS)."""
    return FileResponse(TESTER_HTML_PATH)


@app.get("/", tags=["Health"])
def root():
    """Endpoint simples para checar se a API está no ar."""
    return {"status": "ok", "message": "DevShowcase API está no ar 🚀"}
