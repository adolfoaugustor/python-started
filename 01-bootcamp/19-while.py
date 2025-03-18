# While

'''
while <condition>:
    <do something>
'''

preco_celular = 800
while preco_celular <= 800:
    print('Celular caro')
print(f'Preço do Celular mudou para {preco_celular}')

while True:
    print('Executar alguma coisa')

percorrer_mais_sites = True
while percorrer_mais_sites:
    print('Percorrendo mais sites')
    percorrer_mais_sites = False
    break
print('Acabou')

