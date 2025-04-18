import random
from pprint import pprint

sorteios = ['sorteios1', 'sorteios2', 'sorteios3']
participantes = ['Adolfo', 'Cristian', 'Jorge', 'Lucas', 'Marcos', 'Pedro', 'Rafael', 'Thiago', 'Vinicius']

pprint({sorteio: random.choice(participantes) for sorteio in sorteios})

grupos = ['Grupo1', 'Grupo2', 'Grupo3']
pprint({grupo: [random.randint(1, 100) for _ in range(3)] for grupo in grupos})