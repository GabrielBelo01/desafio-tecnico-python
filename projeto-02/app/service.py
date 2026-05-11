from app.collector import consultar_saldos
from app.repository import salvar_consulta, buscar_ultimos, buscar_historico, buscar_stats
from app.database import SessionLocal

def salvar_consulta_no_banco():
    conexao = SessionLocal()
    saldo_wallets = consultar_saldos()

    for dados in saldo_wallets:
        salvar_consulta(conexao, dados)

    conexao.close()        