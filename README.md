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

data_referencia

taxa

valor_atual
_____________________________________________________
### 🔒 Lógica de Inserção
A DAG busca dados na API do BACEN para um intervalo de datas configurado em utils.py.

Antes de inserir, verifica se a data já existe no banco para evitar duplicações.
_____________________________________________________
### 🧪 Testes
Ainda não implementado.
_____________________________________________________
### 📌 Observações
O banco de dados PostgreSQL é acessado via a conexão postgres configurada no Airflow.

A criação da tabela é automática, não sendo necessária a preparação prévia do banco.

As funções auxiliares para manipulação de datas e códigos de taxa estão no arquivo utils/utils.py.

