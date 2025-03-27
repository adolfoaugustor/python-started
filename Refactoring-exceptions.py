import logging

logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    format='%(levelname)s %(asctime)s: %(message)s\n',
    datefmt='%d-%m-%Y %H:%M:%S'

)

logger = logging.StreamHandler()
logging.getLogger('').addHandler(logger)

try:
    ano_atual = int(input("Digite o ano atual: "))
except ValueError:
    logging.warning("Ano inválido. Por favor, insira um número inteiro.")

try:
    print(10 / 0)
except ZeroDivisionError:
    logging.warning("Não é possível dividir por zero.")


try:
    print(10 / 0)
except:
    logging.warning("Ocorreu um erro inesperado.")

try:
    print(10 / 0)
except:
    logging.warning("Ocorreu um erro")
finally:
    logging.info("Isso sempre será executado, independentemente de um erro ter ocorrido ou não.")

# for pagina in range(10):
#     try:
#         print("buscando a página")
#         print(5/0)
#     except:
#         pass