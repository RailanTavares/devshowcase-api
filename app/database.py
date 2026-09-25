import os
<<<<<<< HEAD
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

=======
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

>>>>>>> 2e8eda9a8d67dc8a2cbc43f1b17f27ba98712a70
# Por padrão, usamos SQLite local (zero configuração, ótimo para desenvolvimento/testes).
# Para usar PostgreSQL, defina a variável de ambiente DATABASE_URL, por exemplo:
#   postgresql://usuario:senha@localhost:5432/devshowcase
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./devshowcase.db")

<<<<<<< HEAD
# SQLAlchemy 1.4+ requer 'postgresql://' e não 'postgres://'
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

=======
>>>>>>> 2e8eda9a8d67dc8a2cbc43f1b17f27ba98712a70
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(DATABASE_URL, connect_args=connect_args)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """Dependency do FastAPI: fornece uma sessão de banco de dados por requisição."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
