from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import repository
from app.schemas import ConsultaResponse, StatsResponse

app = FastAPI()

@app.get("/balances/latest", response_model=list[ConsultaResponse])
def get_latest(db: Session = Depends(get_db)):
    return repository.buscar_ultimos(db)

@app.get("/balances/{wallet}/history", response_model=list[ConsultaResponse])
def get_history(wallet: str, limit: int = 100, db: Session = Depends(get_db)):
    return repository.buscar_historico(db, wallet)

@app.get("/stats", response_model=StatsResponse)
def get_stats(db: Session = Depends(get_db)):
    return repository.buscar_stats(db)    