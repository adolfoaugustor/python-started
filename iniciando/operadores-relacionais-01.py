"""
Operadores relacionais
== igual
> maior que
>= maior igual
<= menor igual
< menor que
!= diferente de
"""

num_1 = 2
num_2 = 3
expressao = num_1 <= num_2

print(expressao)
print('_______________________________________')

nome = input('Qual seu nome?')
idade = input('Qual sua idade?')
idade_limite = 18

if int(idade) >= 18:
    print(f"{nome} é de maior, tem {idade} anos, pode solicitar empréstimo!")
else:
    print(f"{nome} é de menor, tem {idade} anos, não pode solicitar empréstimo!")