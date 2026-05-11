from app.database import engine
from app.models import Base
from app.service import salvar_consulta_no_banco

Base.metadata.create_all(engine)
salvar_consulta_no_banco()
print("Coleta finalizada com sucesso!")