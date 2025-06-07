from datetime import datetime
from dateutil.relativedelta import relativedelta

def get_Dt_ini():
    return (datetime.now() - relativedelta(months=3)).strftime("%d/%m/%Y")

def get_Dt_fim():
    return datetime.now().strftime("%d/%m/%Y")

cods_mercado = {
    'CDI': 4389,
    'Dolar Compra': 10813,
    'Dolar': 1,
    'IGPM': 189,
    'INPC': 188,
    'IPCA': 433,
    'SELIC': 432,
    'TLP': 27572
}
