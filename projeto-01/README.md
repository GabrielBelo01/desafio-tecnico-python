# Projeto 1 - Script de Consulta BSC

## Sobre o projeto

Script Python que se conecta à BSC (Binance Smart Chain) via web3.py e consulta informações de uma wallet pública.

O que ele faz:
- Conecta a um nó RPC da BSC com fallback automático
- Exibe o número do bloco atual da rede
- Consulta o saldo de BNB nativo da wallet
- Consulta o saldo de um token BEP-20 (USDT) da mesma wallet

## Pré-requisitos

- Python 3.8 ou superior
- pip

## Como configurar

1. Clone o repositório
2. Crie e ative o ambiente virtual:
```bash
python -m venv venv
source venv/Scripts/activate  
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Crie um arquivo `.env` na raiz do projeto baseado no `.env.example`:
```
RPC_URL_1=
RPC_URL_2=
WALLET=
TOKEN_ADDRESS=
```

- `RPC_URL_1` e `RPC_URL_2` — endpoints de acesso à BSC (o segundo é o fallback)
- `WALLET` — endereço da wallet pública a ser consultada
- `TOKEN_ADDRESS` — endereço do contrato do token BEP-20 a ser consultado

## Como rodar

```bash
python main.py
```

## Exemplo de saída

```
Conectando no RPC: https://bsc-dataseed.binance.org/
Bloco atual: 97191400
Saldo BNB em wei: 6289749287960118437340922
Saldo BNB: 6,289,749.2880 BNB
Saldo USDT: 1.3162 USDT
```

