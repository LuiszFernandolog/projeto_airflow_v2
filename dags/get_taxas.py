from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime
import requests

from utils.utils import get_Dt_ini, get_Dt_fim, cods_mercado

dag = DAG(
    'taxas_mercado',
    description='Faz a requisição dos dados na API do governo e salva em um banco de dados',
    schedule_interval="0 9-19 * * *",
    start_date=datetime(2023, 3, 5),
    catchup=False
)

#Intervalo de datas para consulta na API
dt_ini = get_Dt_ini()
dt_fim = get_Dt_fim()



#Function que puxa quais datas já existem no banco de dados
def select_data(nome_taxa):
    pg_hook = PostgresHook(postgres_conn_id='postgres')
    records = pg_hook.get_records(f"""select distinct data_referencia from  tx_mercado where taxa = '{nome_taxa}';""")

    return records

#Function para criação da tabela, isso se ela não existir !
def create_table():
    pg_hook = PostgresHook(postgres_conn_id='postgres')
    pg_hook.run("""
        CREATE TABLE IF NOT EXISTS tx_mercado (
            data_referencia varchar,
            taxa VARCHAR(20),
            valor_atual FLOAT
        );""", autocommit=True)

#Função para inserir os dados na tabela criada
def query_and_insert():
    pg_hook = PostgresHook(postgres_conn_id='postgres')
    conn = pg_hook.get_conn()
    cursor = conn.cursor()

    for nome_taxa, cod_taxa in cods_mercado.items():
        url = f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{cod_taxa}/dados?formato=json&dataInicial={dt_ini}&dataFinal={dt_fim}'
        response = requests.get(url)
        dados = response.json()

        #Conjunto com as datas existentes no banco para essa taxa
        datas_existentes = set(row[0] for row in select_data(nome_taxa))

        registros = []
        for linha in dados:
            data_ref = linha['data']
            if data_ref not in datas_existentes:
                valor = float(linha['valor'].replace(',', '.'))
                registros.append((data_ref, nome_taxa, valor))

        if registros:
            cursor.executemany(
                "INSERT INTO tx_mercado (data_referencia, taxa, valor_atual) VALUES (%s, %s, %s)",
                registros
            )
            conn.commit()

    cursor.close()
    conn.close()




#Tasks 

task_create = PythonOperator(
    task_id='create_table',
    python_callable=create_table,
    dag=dag
)

task_query = PythonOperator(
    task_id='query_and_insert',
    python_callable=query_and_insert,
    dag=dag
)


#Ordem das tasks
task_create >> task_query 
