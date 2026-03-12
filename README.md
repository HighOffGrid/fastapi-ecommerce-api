
# FastAPI Ecommerce API


API de ecommerce desenvolvida com FastAPI, utilizando autenticação JWT, banco PostgreSQL e cache com Redis.

Projeto criado para estudo de arquitetura backend moderna.

Tecnologias
	•	FastAPI
	•	PostgreSQL
	•	SQLAlchemy
	•	Alembic (migrations)
	•	Redis (cache)
	•	JWT Authentication
	•	Passlib / Bcrypt (hash de senha)
	•	Pydantic
	•	Python-dotenv
	•	Uvicorn

Funcionalidades
	•	Cadastro de usuários
	•	Autenticação com JWT
	•	Listagem de produtos
	•	Criação de pedidos
	•	Cache com Redis
	•	Migrations com Alembic


## Arquitetura


Client
  |
FastAPI
  |
Service Layer
  |
PostgreSQL


## Rodando o projeto


Clone o repositório:
git clone https://github.com/seuuser/fastapi-ecommerce-api

Instale as dependências:
pip install -r requirements.txt


## Rodando com Docker


docker compose up --build


## Execute a API:


uvicorn main:app --reload


## Documentação da API


Swagger UI:
http://127.0.0.1:8000/docs

ReDoc:
http://127.0.0.1:8000/redoc


## Estrutura do projeto


app/
 ├── models
 ├── schemas
 ├── services
 ├── repositories
 ├── routers
 └── core


## Objetivo


Este projeto foi desenvolvido para prática de desenvolvimento backend utilizando FastAPI e boas práticas de arquitetura.
