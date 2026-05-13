# Desafio Técnico Python — BSC

Desafio técnico desenvolvido em Python com foco em integração com a Binance Smart Chain (BSC), pipeline de dados e visualização. Composto por 3 projetos independentes desenvolvidos em 7 dias.

## Projetos

### [Projeto 01 — Consulta de Saldos](./projeto-01/)
Script Python que conecta na BSC via RPC e consulta o saldo de BNB nativo e token USDT (BEP-20) de uma wallet configurada via `.env`.

**Tecnologias:** Python, web3.py, python-dotenv

---

### [Projeto 02 — Pipeline + API REST](./projeto-02/)
Pipeline de coleta automática de saldos de 3 wallets Binance, com armazenamento em PostgreSQL e exposição via API REST com FastAPI.

**Tecnologias:** Python, web3.py, FastAPI, SQLAlchemy, PostgreSQL, Docker

---

### [Projeto 03 — Dashboard Grafana](./projeto-03/)
Dashboard de monitoramento com 7 painéis, lendo diretamente do banco PostgreSQL com mais de 1.500 registros coletados automaticamente a cada 5 minutos.

**Tecnologias:** Grafana, PostgreSQL, SQL

---

## Tecnologias utilizadas

- Python 3.12
- web3.py
- FastAPI + Uvicorn
- SQLAlchemy
- PostgreSQL (Docker)
- Grafana (Docker)
- Docker Desktop
- DBeaver
- VSCode

---

## Referências de estudo

### Blockchain e web3.py
- [Introdução ao web3.py — Dapp University](https://www.dappuniversity.com/articles/web3-py-intro)
- [O que é Blockchain? — AWS](https://aws.amazon.com/pt/what-is/blockchain/)
- [web3.py Quickstart — Documentação oficial](https://web3py.readthedocs.io/en/stable/quickstart.html)
- [web3.py Providers — Documentação oficial](https://web3py.readthedocs.io/en/stable/providers.html)
- [web3.eth — Documentação oficial](https://web3py.readthedocs.io/en/stable/web3.eth.html)
- [web3.contract — Documentação oficial](https://web3py.readthedocs.io/en/stable/web3.contract.html)

### Vídeos — YouTube
- [Blockchain explicado](https://www.youtube.com/watch?v=ZE2HxTmxfrI)
- [Python e Blockchain](https://www.youtube.com/watch?v=iMOeP4sMhXU)
- [FastAPI do zero](https://www.youtube.com/watch?v=GEhOs6L22Wg&t=210s)
- [FastAPI com banco de dados](https://www.youtube.com/watch?v=wgAMF3zITck)
- [SQLAlchemy com PostgreSQL](https://www.youtube.com/watch?v=qQjIKIRqQkM)
- [Docker para iniciantes](https://www.youtube.com/watch?v=dZid_N5i6Tg)
- [Grafana com PostgreSQL](https://www.youtube.com/watch?v=dkElPTevoR4)
- [Dashboard Grafana do zero](https://www.youtube.com/watch?v=ztQEaQ06GYs&t=1020s)
- [Queries SQL no Grafana](https://www.youtube.com/watch?v=0Mt16eeCv78)

### Ferramentas de apoio
- [Claude — Anthropic](https://claude.ai/)
- [ChatGPT — OpenAI](https://chatgpt.com/)
