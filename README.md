# Bancos de Dados NoSQL - Tweets

Projeto de estudo sobre bancos de dados NoSQL e MongoDB para disciplina de Sistemas NoSQL e BigData da Pós-Gradução em Ciência de Dados e Analytics da PUC-Rio.

## Como fazer o setup do projeto?

O primeiro passo é iniciar uma container Docker com uma imagem pública do MongoDB que vai poder ser acessada na porta 27017:

``` bash

docker run --name mongodb -p 27017:27017 -d mongo

```

Após isso, podemos executar o script Pytgon que carrega os dados iniciais `tweets.json` e faz as operações exigidas pela tarefa.

O projeto utiliza a biblioteca `pymongo` como sua única dependência. Para instalar a mesma versão que utilizei e garantir a reprodução das tarefas, a biblioteca pode ser instalada seguindo as instruções abaixo:

```bash

python3 -m venv env
source env/bin/activate
python -m pip install -r requirements.txt

```

```bash

python main.py

```

```json

[
  {
    "id": 1,
    "username": "user1",
    "tweet": "Primeiro tweet!",
    "likes": 10
  },
  {
    "id": 2,
    "username": "user2",
    "tweet": "Segundo tweet!",
    "likes": 15
  },
  {
    "id": 3,
    "username": "user3",
    "tweet": "Mais um tweet!",
    "likes": 5
  }
]


```

## Exercícios

Usando o arquivo importado e com pesquisa na documentação do MongoDB, execute:

- Pesquisa pelos tweets com número de likes maior ou igual a 10;

- Inserção de 50 tweets, usando somente os usuários user1, user2 e user3, mas variando o texto e o número de likes, que pode ser um número qualquer entre 1 e 100;

- Atualização de todos os tweets do user1, somando-se 5 ao número de likes correspondente;

- Remoção de todos os tweets de user3 com número de likes menor que 10.