from datetime import datetime

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')
ano = datetime.now().year

ano_nascimento = ano - int(idade)

print(f'{nome} tem {idade} anos e nasceu em {ano_nascimento}')