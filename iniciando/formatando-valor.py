'''
Formatando valor com modificadores
:s - Texto (strings)
:d - Inteiros (int)
:f - numeros de ponto flutuante (float)
:.(número)f - Quantidade de casas decimais (float)
:(caractere) ( > ou < ou ^ ) (Quantidade) (tipo - s, d ou f)

> -  esquerda
< -  direita
^ - Centro
'''

# num_1 = 1
# print(f'{num_1:0>10}')
# num_2 = 2
# print(f'{num_2:0<10}')
# num_3 = 3
# print(f'{num_3:0^10}')
# num_4 = 4
# print(f'{num_4:0>10.2f}')
nome = "Adolfo Augusto"
# print((50-nome.__len__())/2)
# print(f'{nome:#^50}')
nome_formatado = '{n:0<20}'.format(n=nome)
print(nome_formatado)
print(nome.lower())
print(nome.upper())
print(nome.title())