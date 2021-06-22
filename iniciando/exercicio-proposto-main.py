#primeiro exercício
# numero = input('Digite um número: ')
#
# if numero.isdigit():
#     numero = int(numero)
#     if (numero % 2) == 0:
#         print("o Número é Par")
#     else:
#         print("o Número é Ímpar")
# else:
#     print('Apenas números inteiros.')
#_________________________________________________________________________________
# import datetime
# hora = input("que horas são? ")
#
# if (hora.split(':')[0]).isdigit() and (hora.split(':')[1]).isdigit():
#     hora_1 = int(hora.split(':')[0])
#     minuto = int(hora.split(':')[1])
#
#     if hora_1 >= 0 or hora_1 <= 11:
#         print(f'Bom dia, são {hora_1}:{minuto}!')
#     elif hora_1 >= 12 or hora_1 <= 17:
#         print(f'Boa tarde, são {hora_1}:{minuto}!')
#     elif hora_1 >= 18 or hora_1 <= 23:
#         print(f'Boa noite, são {hora_1}:{minuto}!')
#     else:
#         print('hora informada inválida!')
# else:
#     print('hora informada inválida!')

#_________________________________________________________________________________
# nome = input('Escreva seu nome: ')
# nome = int(nome.__len__())
#
# if nome <= 4:
#     print('Seu nome é curto!')
# elif nome >= 5 and nome <= 6:
#     print('Seu nome é normal!')
# elif nome > 6:
#     print('Seu nome é grande!')