from app.models import Consulta
from sqlalchemy import text

def salvar_consulta (db, dados):
    consulta = Consulta(
        wallet=dados["wallet"],
        token=dados["token"],
        saldo=dados["saldo"]
    )
    db.add(consulta)

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

    variacao = db.execute(text("""
        SELECT
            wallet,
            ROUND(
                ((saldo_atual - saldo_anterior) / NULLIF(saldo_anterior, 0) * 100)::numeric,
                2
            ) AS variacao_percentual
        FROM (
            SELECT
                wallet,
                FIRST_VALUE(saldo) OVER (PARTITION BY wallet ORDER BY coletado_em DESC) AS saldo_atual,
                FIRST_VALUE(saldo) OVER (PARTITION BY wallet ORDER BY coletado_em ASC) AS saldo_anterior,
                ROW_NUMBER() OVER (PARTITION BY wallet ORDER BY coletado_em DESC) AS rn
            FROM consultas
            WHERE coletado_em >= NOW() - INTERVAL '24 hours'
        ) sub
        WHERE rn = 1
    """)).mappings().all()

    return {
        "wallet_maior_saldo": maior,
        "variacao_24h": [dict(v) for v in variacao]
    }
   