from datetime import datetime

nome = 'Adolfo Augusto'
idade = 31
altura = 1.67
peso = 80
e_maior = idade > 18
imc = peso / (altura ** 2)
ano = datetime.now().year
nascimento = ano - idade


print(f'{nome}, tem {idade} anos de idade, seu imc é {imc:.2f}, altura {altura}')
print(f'nasceu em {nascimento}')