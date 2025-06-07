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


projeto_airflow_v2/
├── dags/ # DAGs definidas no Airflow
│ └── dag_taxas.py # DAG principal para coleta de taxas
├── utils/ # Funções auxiliares (datas, selects, dicionários)
│ └── utils.py
├── docker-compose.yml # Configuração dos containers
├── requirements.txt # Dependências do projeto
└── README.md # Este documento

_____________________________________________________


## ⚙️ Como rodar o projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/LuiszFernandolog/projeto_airflow_v2.git
cd projeto_airflow_v2
