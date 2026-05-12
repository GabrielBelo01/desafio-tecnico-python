from web3 import Web3
from dotenv import load_dotenv
from decimal import Decimal
import os

load_dotenv()

rpc_1 = os.getenv("RPC_URL_1")
rpc_2 = os.getenv("RPC_URL_2")

wallet_1 = os.getenv("WALLET_1")
wallet_2 = os.getenv("WALLET_2")
wallet_3 = os.getenv("WALLET_3")

token_address = os.getenv("TOKEN_ADDRESS")

def conectar_rpc(rpc_1, rpc_2):
    for url in [rpc_1, rpc_2]:
        w3 = Web3(Web3.HTTPProvider(url))
        
        if w3.is_connected():
            print(f"Conectando no RPC: {url}")
            return w3

    raise Exception("Nenhum RPC disponivel")


ABI = [
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "decimals",
        "outputs": [{"name": "", "type": "uint8"}],
        "type": "function"
    }
]


def consultar_saldos():
    w3 = conectar_rpc(rpc_1, rpc_2)
    contrato = w3.eth.contract(address=token_address, abi=ABI)
    decimals = contrato.functions.decimals().call()
    
    wallets = [wallet_1, wallet_2, wallet_3]
    resultados = []

    for wallet in wallets:
        saldo_bruto = contrato.functions.balanceOf(wallet).call()
        saldo = Decimal(saldo_bruto) / Decimal(10 ** decimals)
        resultados.append({
            "wallet": wallet,
            "saldo": saldo,
            "token": token_address
        })

    return resultados
