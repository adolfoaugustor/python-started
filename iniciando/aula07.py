nome = 'Adolfo Augusto'
idade = 31
altura = 1.67
e_maior = idade > 18
peso = 80
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print(f'{nome}, tem {idade} anos de idade, seu imc é {imc:.2f}')
print('{0}, tem {1} anos, seu imc é {2}'.format(nome, idade, imc))
print('{n}, tem {i} anos, seu imc é {im}'.format(n=nome, i=idade, im=imc))