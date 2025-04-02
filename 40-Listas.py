#criar listas

# numeros = []
# for i in range(10):
#    numeros.append(i)
# print(numeros)

nomes = ['Lucas', 'João', 'Maria', 'Ana']

def aprovar_pessoa(nome):
   return nome + ' APROVADO'

print(list(map(aprovar_pessoa, nomes)))