from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import repository

app = FastAPI()

@app.get("/balances/latest")
def get_latest(db: Session = Depends(get_db)):
    return repository.buscar_ultimos(db)

@app.get("/balances/{wallet}/history")
def get_history(wallet: str, db: Session = Depends(get_db)):
    return repository.buscar_historico(db, wallet)

@app.get("/stats")
def get_stats(db: Session = Depends(get_db)):
    return repository.buscar_stats(db)    