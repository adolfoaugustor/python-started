# x = 0
# while x <= 10:
#     if x == 3: # excluí o 3 pra não exibir no contador
#         x += 1
#         continue
#         #break finaliza o while
#
#     print(x)
#     x += 1
#
# print('Acabou')

#Calculadora
while True:
    print('#Calculadora: ')
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    operador = input('operador aritimético?')

    if not num1.isnumeric() or not num2.isnumeric():
        print('Você precisa digitar um número!')
        continue

    num1 = int(num1)
    num2 = int(num2)

    if operador == '+':
        print(num1 + num2)
    elif operador == '-':
        print(num1 - num2)
    elif operador == '/':
        print(num1 - num2)
    elif operador == '*':
        print(num1 * num2)
    else:
        print('Operador inválido!')

    sair = input('Deseja sair? [s]im ou [n]ão ')
    if sair == 's':
        break