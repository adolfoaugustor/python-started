# try:
#     ano_atual = int(input("Digite o ano atual: "))
# except ValueError:
#     print("Ano inválido. Por favor, insira um número inteiro.")

# try:
#     print(10 / 0)
# except ZeroDivisionError:
#     print("Não é possível dividir por zero.")

# try:
#     print(10 / 0)
# except:
#     print("Ocorreu um erro inesperado.")

# try:
#     print(10 / 0)
# except:
#     print("Ocorreu um erro inesperado.")
# finally:
#     print("Isso sempre será executado, independentemente de um erro ter ocorrido ou não.")

for pagina in range(10):
    try:
        print("buscando a página")
        print(5/0)
    except:
        pass