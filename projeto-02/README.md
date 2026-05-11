# Projeto 2 - Pipeline + Backend FastAPI

## Sobre o projeto

Script Python que consulta o saldo de 3 wallets públicas da Binance em um token BEP-20, salva os dados em um banco PostgreSQL e expõe as informações via uma API REST construída com FastAPI.

## Arquitetura

```
collector.py  →  consulta saldos na BSC via web3.py
service.py    →  orquestra a coleta e o salvamento
repository.py →  operações no banco de dados
database.py   →  conexão com o PostgreSQL via SQLAlchemy
models.py     →  definição da tabela no banco
api.py        →  endpoints FastAPI
```

Fluxo de dados:
```
BSC (blockchain)
      ↓
collector.py (consulta saldos)
      ↓
service.py (orquestra)
      ↓
repository.py (salva no banco)
      ↓
PostgreSQL
      ↓
api.py (expõe os dados)
```

## Pré-requisitos

- Python 3.11+
- Docker

## Como configurar

1. Clone o repositório
2. Entre na pasta do projeto:
```bash
cd projeto-02
```

3. Crie e ative o ambiente virtual:
```bash
python -m venv venv
source venv/Scripts/activate 
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

5. Crie o arquivo `.env` baseado no `.env.example`:
```
RPC_URL_1=
RPC_URL_2=

WALLET_1=
WALLET_2=
WALLET_3=
TOKEN_ADDRESS=

DB_HOST=
DB_PORT=
DB_NAME=
DB_USER=
DB_PASSWORD=
```

## Como subir o banco

Suba o container PostgreSQL com Docker:
```bash
docker run --name postgres \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=bsc_coletas \
  -p 5432:5432 \
  -d postgres
```

## Como rodar o coletor

O coletor consulta os saldos na BSC e salva no banco. Para rodar:

```bash
python run_collector.py
```

## Como subir a API

```bash
uvicorn app.api:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`
O Swagger estará disponível em `http://127.0.0.1:8000/docs`

## Endpoints

| Método | Rota | Descrição |
|---|---|---|
| GET | `/balances/latest` | Último saldo de cada wallet monitorada |
| GET | `/balances/{wallet}/history` | Histórico de uma wallet específica |
| GET | `/stats` | Wallet com maior saldo |
