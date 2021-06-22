#primeiro exercício
numero = input('Digite um número: ')

if numero.isdigit():
    numero = int(numero)
    if (numero % 2) == 0:
        print("o Número é Par")
    else:
        print("o Número é Ímpar")
else:
    print('Apenas números inteiros.')