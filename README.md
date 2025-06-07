# Projeto Airflow V2

Este projeto utiliza o Apache Airflow para extrair dados de taxas de mercado da API do Banco Central e armazená-los em um banco de dados PostgreSQL.

## 📦 Objetivo
Automatizar a coleta e persistência de indicadores econômicos como CDI, Dólar, IPCA, SELIC, entre outros.

## 🚀 Tecnologias
- Python
- Apache Airflow
- PostgreSQL
- Docker (Docker Compose)
- API Bacen (https://dadosabertos.bcb.gov.br/)

## 🔧 Estrutura do Projeto

```bash
projeto_airflow_v2/
├── dags/                  # DAGs definidas no Airflow
│   └── dag_taxas.py       # DAG principal para coleta de taxas
├── utils/                 # Funções auxiliares (datas, selects, dicionários)
│   └── utils.py
├── docker-compose.yml     # Configuração dos containers
├── requirements.txt       # Dependências do projeto
└── README.md              # Documentação principal
```
_____________________________________________________


## ⚙️ Como rodar o projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/LuiszFernandolog/projeto_airflow_v2.git
cd projeto_airflow_v2
```

### 2. Subir os containers com Docker

```bash
docker-compose up --build
```
*Aguarde o Airflow inicializar totalmente (leva alguns segundos na primeira vez).

### 3. Acessar a interface do Airflow
URL: http://localhost:8080

Usuário: airflow

Senha: airflow

### 4. Ativar a DAG
No painel do Airflow, ative a DAG chamada taxas_mercado2 para iniciar a coleta dos dados.
_____________________________________________________

📈 Resultados Esperados
O projeto irá criar automaticamente a tabela tx_mercado no PostgreSQL, com os seguintes campos:

-data_referencia

-taxa

-valor_atual
_____________________________________________________
### 🔒 Lógica de Inserção
A DAG busca dados na API do BACEN para um intervalo de datas configurado em utils.py.

Antes de inserir, verifica se a data já existe no banco para evitar duplicações.
_____________________________________________________
### 🧪 Testes
*De acordo com o arquivo get_taxas.py, o scheduler foi definido pra rodar a partir das 09hrs até às 19hrs, sendo executado a cada 1 hora. Isso porque as taxas não têm o mesmo horário para atualizar.

Graph da task:

![image](https://github.com/user-attachments/assets/26b5dc19-6546-4d52-a099-a5d386da442a)


Inserção(select - simples):

![image](https://github.com/user-attachments/assets/1005fd4a-306f-4fdf-b92d-9a60edbd4497)



![image](https://github.com/user-attachments/assets/c2d472b6-581c-429f-a8a6-3532b506effa)

_____________________________________________________
### 📌 Observações
O banco de dados PostgreSQL é acessado via a conexão postgres configurada no Airflow.

A criação da tabela é automática, não sendo necessária a preparação prévia do banco.

As funções auxiliares para manipulação de datas e códigos de taxa estão no arquivo utils/utils.py.

