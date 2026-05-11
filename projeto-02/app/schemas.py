from pydantic import BaseModel
from datetime import datetime

class ConsultaResponse(BaseModel):
    id: int
    wallet: str
    token: str
    saldo: float
    coletado_em: datetime

    class Config:
        from_attributes = True

class WalletSaldo(BaseModel):
    wallet: str
    saldo: float

class StatsResponse(BaseModel):
    wallet_maior_saldo: WalletSaldo     
