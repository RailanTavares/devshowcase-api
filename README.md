# DevShowcase API

API REST para uma plataforma de vitrine de projetos de desenvolvedores. Permite cadastrar perfis, tecnologias, projetos e feedbacks, com relacionamentos entre eles.

## Stack utilizada

- **Python 3.11+**
- **FastAPI** — framework web
- **SQLAlchemy** — ORM / camada de acesso a dados
- **Pydantic** — validação de DTOs (entrada e saída)
- **SQLite** (padrão, zero configuração) ou **PostgreSQL** (via variável de ambiente)
- **Uvicorn** — servidor ASGI

## Modelagem de entidades

| Entidade   | Descrição                          |
|------------|-------------------------------------|
| Profile    | Perfil do desenvolvedor             |
| Project    | Projeto cadastrado por um perfil    |
| Technology | Tecnologia usada em projetos        |
| Feedback   | Opinião/avaliação sobre um projeto  |

**Relacionamentos:**
- `Profile 1 : N Project` — um perfil tem vários projetos
- `Project N : N Technology` — um projeto pode usar várias tecnologias, e uma tecnologia pode estar em vários projetos (tabela associativa `project_technology`)
- `Project 1 : N Feedback` — um projeto pode receber vários feedbacks

## Estrutura do projeto

```
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
├── scripts/
│   ├── setup.sh / setup.bat     # cria venv, instala deps e popula o banco
│   ├── run.sh / run.bat         # sobe o servidor rapidamente
│   ├── reset_db.sh              # apaga e recria os dados de exemplo
│   └── seed_data.py             # popula o banco com dados de exemplo
├── requirements.txt
├── .gitignore
├── .env.example
└── README.md
```

## Início rápido (automatizado) — recomendado para gravar o vídeo

Rode um único comando para criar o ambiente, instalar as dependências e já popular
o banco com um perfil, tecnologias, um projeto e um feedback de exemplo:

```bash
# Linux/Mac
bash scripts/setup.sh

# Windows
scripts\setup.bat
```

Depois, para subir o servidor:

```bash
# Linux/Mac
bash scripts/run.sh

# Windows
scripts\run.bat
```

Se quiser resetar o banco (apagar tudo e recriar os dados de exemplo do zero) antes
de gravar novamente:

```bash
bash scripts/reset_db.sh
```

Os dados de exemplo já vêm com IDs previsíveis (perfil id 1, tecnologias 1 a 4,
projeto id 1), que já estão pré-configurados na coleção do Postman
(`DevShowcase_API.postman_collection.json`) — assim você pode ir direto para o
`GET /api/profiles/1`, `GET /api/technologies` e `GET /api/projects` sem precisar
criar nada na hora da gravação. Ainda assim, recomendamos demonstrar pelo menos um
`POST` de cada recurso ao vivo, para provar que as validações funcionam.

## Como rodar o projeto manualmente

1. Clone o repositório e entre na pasta:
   ```bash
   git clone <URL_DO_SEU_REPOSITORIO>
   cd devshowcase-api
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/Mac
   venv\Scripts\activate         # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. (Opcional) Configure o PostgreSQL: copie `.env.example` para `.env` e defina `DATABASE_URL`. Se não fizer isso, a API usa SQLite automaticamente (`devshowcase.db`).

5. Rode a aplicação:
   ```bash
   uvicorn app.main:app --reload
   ```

6. Acesse a documentação interativa (Swagger) em:
   ```
   http://127.0.0.1:8000/docs
   ```

## Endpoints implementados

| Método | Rota                        | Descrição                              |
|--------|-----------------------------|-----------------------------------------|
| POST   | `/api/profiles`             | Cadastra um perfil                      |
| GET    | `/api/profiles/{id}`        | Busca um perfil por ID                  |
| POST   | `/api/technologies`         | Cadastra uma tecnologia                 |
| GET    | `/api/technologies`         | Lista todas as tecnologias              |
| POST   | `/api/projects`             | Cadastra um projeto                     |
| GET    | `/api/projects`             | Lista todos os projetos                 |

### Exemplos de requisição (curl)

**Cadastrar perfil:**
```bash
curl -X POST http://127.0.0.1:8000/api/profiles \
  -H "Content-Type: application/json" \
  -d '{
    "full_name": "Maria Silva",
    "email": "maria@email.com",
    "bio": "Desenvolvedora fullstack",
    "github_url": "https://github.com/mariasilva"
  }'
```

**Cadastrar tecnologia:**
```bash
curl -X POST http://127.0.0.1:8000/api/technologies \
  -H "Content-Type: application/json" \
  -d '{"name": "FastAPI"}'
```

**Cadastrar projeto:**
```bash
curl -X POST http://127.0.0.1:8000/api/projects \
  -H "Content-Type: application/json" \
  -d '{
    "title": "DevShowcase API",
    "description": "Backend do projeto da faculdade",
    "repository_url": "https://github.com/mariasilva/devshowcase-api",
    "profile_id": 1,
    "technology_ids": [1]
  }'
```

## Validações implementadas

- `full_name`, `email`: obrigatórios no cadastro de perfil (e-mail validado por formato).
- `title`: obrigatório e não pode ser vazio/apenas espaços no cadastro de projeto.
- `repository_url`, `demo_url`, `github_url`, `avatar_url`: validados como URLs válidas (HttpUrl do Pydantic).
- `name` da tecnologia: obrigatório, não vazio.
- Regras de negócio: não permite dois perfis com o mesmo e-mail, nem duas tecnologias com o mesmo nome; não permite criar projeto para um perfil inexistente.

## Testando com Postman

Importe o arquivo `DevShowcase_API.postman_collection.json` (na raiz do projeto) no Postman para testar todos os endpoints já configurados.

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
