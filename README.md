# FastAPI E-commerce API

API backend de e-commerce desenvolvida com FastAPI, com autenticação JWT, catálogo de produtos e gestão de pedidos.

**Stack:** Python · FastAPI · PostgreSQL · SQLAlchemy · Alembic · Docker

---

## Funcionalidades

- Cadastro e login de usuários com JWT
- Hash seguro de senha
- CRUD de produtos
- Criação e consulta de pedidos
- Persistência com PostgreSQL
- Migrations com Alembic
- Documentação automática com Swagger e ReDoc
- Configuração por variáveis de ambiente

---

## Como executar

```bash
git clone [https://github.com/HighOffGrid/fastapi-ecommerce-api.git](https://github.com/HighOffGrid/fastapi-ecommerce-api.git)
cd fastapi-ecommerce-api
cp .env.example .env
docker compose up --build
```

No Windows PowerShell:

```powershell
Copy-Item .env.example .env
docker compose up --build
```

Acesse:

- Swagger: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

---

## Segurança

- Senhas armazenadas com hash seguro
- JWT para rotas protegidas
- Segredos configurados por variáveis de ambiente
- Validação de entrada e saída com Pydantic

---

## Próximos passos

- Adicionar testes automatizados
- Criar CI com GitHub Actions
- Revisar autorização de pedidos para garantir que cada usuário veja apenas os próprios dados
