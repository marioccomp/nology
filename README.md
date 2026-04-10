# Desafio Nology

Solução desenvolvida para o desafio técnico da Nology: uma calculadora de cashback com backend em FastAPI, frontend estático e persistência das consultas em PostgreSQL.

Aplicação publicada: [https://nology-1.onrender.com/](https://nology-1.onrender.com/)

## O que foi desenvolvido

- backend em FastAPI para cálculo e consulta de cashback
- frontend em HTML, CSS e JavaScript puro
- persistência das consultas por IP em PostgreSQL
- resolução isolada da questão 5 em `5_cashback.py`

## Regras de negócio

O cashback segue a ordem abaixo:

1. calcular 5% sobre o valor final pago
2. aplicar 10% de bônus sobre o cashback base para clientes VIP
3. dobrar o cashback final em compras acima de R$ 500

Essa ordem foi mantida porque ela aparece explicitamente no enunciado do desafio.

## Estrutura do projeto

```text
nology/
├── app/                # Backend FastAPI
├── frontend/           # Frontend estático
├── 5_cashback.py       # Resolução da questão 5
├── compose.yaml        # Banco local com Docker
└── .env.example        # Variáveis de ambiente locais
```

## Backend

O backend foi organizado em camadas para separar responsabilidades:

- `routers`: define os endpoints da API
- `services`: concentra a regra de negócio
- `repositories`: faz o acesso ao banco
- `schemas`: valida e serializa os dados
- `models`: define os modelos ORM
- `database`: configura conexão e sessão

Tecnologias usadas:

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL

O backend também utiliza Pydantic para validar os dados recebidos e retornados pela API.

## Frontend

O frontend foi construído com HTML, CSS e JavaScript puro, com foco em um fluxo simples:

- informar o valor final pago
- selecionar o tipo de cliente
- consultar o cashback
- visualizar o histórico das últimas consultas

Optei por pedir diretamente o valor final da compra porque essa é a informação usada pela regra de negócio e isso reduz complexidade para o usuário final.

## Questão 5

A resolução isolada da questão 5 está em `5_cashback.py`, com a lógica de:

- calcular o valor final após desconto
- calcular o cashback conforme as regras do desafio

## Como rodar localmente

1. Instale as dependências:

```bash
pip install -r app/requirements.txt
```

2. Suba o banco com Docker:

```bash
docker compose up -d
```

3. Configure o `.env` com base no `.env.example`.

4. Rode a API:

```bash
cd app
uvicorn main:app --reload
```

Documentação da API:

```text
http://127.0.0.1:8000/docs
```

## Autor

Projeto desenvolvido por Mario para o desafio técnico da Nology.
