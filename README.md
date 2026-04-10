# Desafio Nology

Este repositório contém a solução para o desafio técnico da Nology, incluindo:

- um backend em FastAPI
- um frontend estático em HTML, CSS e JavaScript
- a resolução da questão 5 no arquivo [`5_cashback.py`](C:\Users\mario\OneDrive\Documents\vscode\nology\5_cashback.py)

## Estrutura do projeto

```text
nology/
├── app/                # Backend FastAPI
├── frontend/           # Frontend estático
├── 5_cashback.py       # Resolução da questão 5
├── compose.yaml        # Banco local com Docker
└── .env.example        # Variáveis de ambiente locais
```

## Regras de negócio

O cálculo do cashback segue estas regras:

- o cashback base é 5% do valor final pago
- clientes VIP recebem 10% de bônus sobre o cashback base
- compras acima de R$ 500 recebem o dobro do cashback
- primeiro é calculado o cashback base, depois o bônus VIP

## Aplicação publicada

A aplicação pode ser acessada em:

[https://nology-1.onrender.com/](https://nology-1.onrender.com/)

## Backend

O backend foi desenvolvido com FastAPI e é responsável por:

- calcular o cashback
- registrar as consultas no banco de dados
- listar o histórico das últimas consultas por IP

### Tecnologias

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL

### Como rodar localmente

1. Instale as dependências:

```bash
pip install -r app/requirements.txt
```

2. Suba o banco com Docker:

```bash
docker compose up -d
```

3. Configure o arquivo `.env` com o conteúdo de `.env.example`.


4. Rode a API:

```bash
cd app
uvicorn main:app --reload
```

A documentação da API ficará disponível em:

```text
http://127.0.0.1:8000/docs
```

## Frontend

O frontend foi desenvolvido com:

- HTML
- CSS
- JavaScript puro

Ele permite:

- informar o valor da compra
- selecionar o tipo de cliente
- consultar o cashback
- visualizar o histórico das consultas

## Questão 5

A resolução isolada da questão 5 está no arquivo `5_cashback.py`.

Esse arquivo contém a lógica principal para:

- calcular o valor final após desconto
- calcular o cashback de acordo com as regras do desafio

## Banco de dados

O projeto usa PostgreSQL.

No ambiente local, o banco pode ser iniciado com o arquivo `compose.yaml`.


## Autor

Projeto desenvolvido por Mario para o desafio técnico da Nology.
