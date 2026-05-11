from app.models import Consulta
from sqlalchemy import text

def salvar_consulta (db, dados):
    consulta = Consulta(
        wallet=dados["wallet"],
        token=dados["token"],
        saldo=dados["saldo"]
    )
    db.add(consulta)
    db.commit()

def buscar_ultimos(db):
    resultado = db.execute(text("""
        SELECT DISTINCT ON (wallet) *
        FROM consultas
        ORDER BY wallet, coletado_em DESC
    """))
    return resultado.mappings().all() 

def buscar_historico(db, wallet):
    resultado = db.execute(text("""
        SELECT * FROM consultas
        WHERE wallet = :wallet
        ORDER BY coletado_em DESC
    """), {"wallet": wallet})
    return resultado.mappings().all()

def buscar_stats(db):
    resultados = db.execute(text("""
        SELECT DISTINCT ON (wallet) wallet, saldo
        FROM consultas
        ORDER BY wallet, coletado_em DESC
    """)).mappings().all()

    maior = max(resultados, key=lambda x: x["saldo"])
    return {"wallet_maior_saldo": maior}
   