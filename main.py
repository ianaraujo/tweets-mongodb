import json
import random
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

database = client['testdb']
collection = database['tweets']

collection.delete_many({}) # inicia sempre com a coleção vazia


# 0. Inserir os dados presentes no arquivo tweets.json

with open('tweets.json') as file:
    tweets = json.load(file)
    collection.insert_many(tweets)

results = [document for document in collection.find({}, {'_id' : 0})]

print(json.dumps(results, indent=2))


# 1. Pesquisa pelos tweets com número de likes maior ou igual a 10;

collection.find({ 'likes' : { '$gte' : 10 }})


# 2. Inserção de 50 tweets aleatórios, usando somente os usuários user1, user2 e user3;

def generate_tweets(n=50, skip=4):

    users = ['user1', 'user2', 'user3']

    tweets = [
        {
            'id': i,
            'username': random.choice(users),
            'tweet': f'Tweet número {i}!',
            'likes': random.randint(1, 100)
        }
        
        for i in range(skip, n + skip)
    ]

    return tweets

random_tweets = generate_tweets()

collection.insert_many(random_tweets)
 
print(collection.count_documents({}))


# 3. Atualização de todos os tweets do user1, somando-se 5 ao número de likes;

query_filter = {'username' : 'user1'}
operation = {'$inc' : {'likes' : 5}}

collection.update_many(query_filter, operation)


# 4. Remoção de todos os tweets de user3 com número de likes menor que 10;

query = {
    'username' : 'user3',
    'likes' : {'$lt' : 10}
}

collection.delete_many(query)

print(collection.count_documents({}))

# Fecha a conexão com o banco de dados

client.close()


