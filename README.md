# DevShowcase API

API REST para uma plataforma de vitrine de projetos de desenvolvedores. Permite cadastrar perfis, tecnologias, projetos e feedbacks, com relacionamentos entre eles.

## Stack utilizada

- **Python 3.11+**
- **FastAPI** — framework web
- **SQLAlchemy** — ORM / camada de acesso a dados
- **Pydantic** — validação de DTOs (entrada e saída)
- **SQLite** (padrão, zero configuração) ou **PostgreSQL** (via variável de ambiente)
- **Uvicorn** — servidor ASGI


## Estrutura do projeto

devshowcase-api/
├── app/
│   ├── main.py              # ponto de entrada da aplicação
│   ├── database.py          # configuração do SQLAlchemy (engine/session)
│   ├── models/               # entidades (SQLAlchemy)
│   │   ├── profile.py
│   │   ├── project.py
│   │   ├── technology.py
│   │   └── feedback.py
│   ├── schemas/               # DTOs de entrada/saída (Pydantic)
│   │   ├── profile.py
│   │   ├── project.py
│   │   ├── technology.py
│   │   └── feedback.py
│   ├── crud/                  # camada de acesso a dados (repositórios)
│   │   ├── profile.py
│   │   ├── project.py
│   │   └── technology.py
│   └── routers/                # endpoints REST
│       ├── profiles.py
│       ├── projects.py
│       └── technologies.py
<<<<<<< HEAD
├── scripts/
│   ├── setup.sh / setup.bat     # cria venv, instala deps e popula o banco
│   ├── run.sh / run.bat         # sobe o servidor rapidamente
│   ├── reset_db.sh              # apaga e recria os dados de exemplo
│   └── seed_data.py             # popula o banco com dados de exemplo
=======
>>>>>>> 2e8eda9a8d67dc8a2cbc43f1b17f27ba98712a70
├── requirements.txt
├── .gitignore
├── .env.example
└── README.md

## Endpoints implementados

| Método | Rota                        | Descrição                              |
|--------|-----------------------------|-----------------------------------------|
| POST   | `/api/profiles`             | Cadastra um perfil                      |
| GET    | `/api/profiles/{id}`        | Busca um perfil por ID                  |
| POST   | `/api/technologies`         | Cadastra uma tecnologia                 |
| GET    | `/api/technologies`         | Lista todas as tecnologias              |
| POST   | `/api/projects`             | Cadastra um projeto                     |
| GET    | `/api/projects`             | Lista todos os projetos                 |


## Validações implementadas

- `full_name`, `email`: obrigatórios no cadastro de perfil (e-mail validado por formato).
- `title`: obrigatório e não pode ser vazio/apenas espaços no cadastro de projeto.
- `repository_url`, `demo_url`, `github_url`, `avatar_url`: validados como URLs válidas (HttpUrl do Pydantic).
- `name` da tecnologia: obrigatório, não vazio.
- Regras de negócio: não permite dois perfis com o mesmo e-mail, nem duas tecnologias com o mesmo nome; não permite criar projeto para um perfil inexistente.

## Testando com Postman

Importe o arquivo `DevShowcase_API.postman_collection.json` (na raiz do projeto) no Postman para testar todos os endpoints já configurados.
<<<<<<< HEAD

## Painel de testes visual (alternativa ao Postman)

O arquivo `devshowcase-tester.html` é uma página feita sob medida para os 6
endpoints exigidos pela atividade. A própria API já serve essa página, então
**não abra o arquivo com duplo clique** — isso o abre como `file://`, e
navegadores como o Chrome bloqueiam por segurança ("Private Network Access")
uma página `file://` chamando `http://127.0.0.1`, mesmo com CORS liberado.

Como usar (forma correta):
1. Suba a API normalmente (`scripts/run.sh` ou `scripts\run.bat`).
2. Acesse **http://127.0.0.1:8000/painel** no navegador (não o arquivo local).
3. Confirme que a bolinha de status está verde ("API online").
4. Escolha o endpoint na barra lateral, preencha o formulário e clique em
   enviar — a resposta da API aparece no console abaixo, com o status HTTP.

Essa página é só uma ferramenta extra de demonstração; ela não faz parte da
avaliação da API em si, mas ajuda a mostrar os 6 endpoints de forma mais visual
durante a gravação do vídeo, como alternativa ao Postman.
