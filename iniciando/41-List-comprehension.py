# nova_lista = [2 * i for i in range(10)]
# print(nova_lista)

# List comprehension
# nomes = ['Lucas', 'João', 'Maria', 'Ana']
# print([nome + ' APROVADO' for nome in nomes])
from pprint import pprint
# pprint([[i for i in range(1,6)] for x in range(5)])

# List comprehension with condition
def aprovar_pessoa(nome):
   return nome + ' APROVADO'

nomes = ['Lucas', 'João', 'Maria', 'Ana']
# print([aprovar_pessoa(nome) for nome in nomes if nome != 'Ana'])

# print([i for i in range(20) if i not in (1,5,15,19)])

def par_impar(i):
   if i % 2 == 0:
      return True
   else:
      return False

print([i for i in range(20) if par_impar(i)])