from web3 import Web3
from dotenv import load_dotenv
import os

load_dotenv()

rpc1 = os.getenv("RPC_URL_1")
rpc2 = os.getenv("RPC_URL_2")
wallet = os.getenv("WALLET")
token_address = os.getenv("TOKEN_ADDRESS")


def conectar_rpc(rpc1, rpc2):
    for url in [rpc1, rpc2]:
        w3 = Web3(Web3.HTTPProvider(url))
        if w3.is_connected():
            print(f"Conectando no RPC: {url}")
            return w3
    raise Exception("Nenhum RPC disponivel")

w3 = conectar_rpc(rpc1,rpc2)

bloco_atual = w3.eth.block_number
print(f"Bloco atual: {bloco_atual}")

saldo_wei = w3.eth.get_balance(wallet)
saldo_bnb = w3.from_wei(saldo_wei, "ether")
print(f"Saldo BNB em wei: {saldo_wei}")
print(f"Saldo BNB: {saldo_bnb:,.4f} BNB")

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

contrato = w3.eth.contract(address=token_address, abi=ABI)
decimals = contrato.functions.decimals().call()
saldo_token_bruto = contrato.functions.balanceOf(wallet).call()
saldo_token = saldo_token_bruto / 10 ** decimals

print(f"Saldo USDT: {saldo_token:.4f} USDT")