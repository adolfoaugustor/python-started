# Dicionarios

from ast import List


pessoa = ["Adolfo", 35, 1.66]
# print(pessoa[0])

# pessoa = {'nome': 'Adolfo', 'idade': 35, 'altura': 1.66}
# print(pessoa['nome'])
# print(pessoa['idade'])
# print(pessoa['altura'])

# filme = dict(nome='Star Wars', ano=1977, diretor='George Lucas')
# print(filme)

nomes = ["Adolfo", "Ana", "Bia", "Carlos", "Adolfo"]
# print(nomes)
print(list(dict.fromkeys(nomes)))
