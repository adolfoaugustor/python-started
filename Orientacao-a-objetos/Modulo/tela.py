# module

def definir_claridade_da_tela(claridade):
    """Define a claridade da tela"""
    if claridade == 1:
        print("Tela clara")
    elif claridade == 2:
        print("Tela escura")
    else:
        print("Claridade inválida")


def definir_desligamento_uatomatico(time):
    """Define o tempo de desligamento automático"""
    if time == 1:
        print("Desligamento automático em 5 minutos")
    elif time == 2:
        print("Desligamento automático em 10 minutos")
    elif time == 3:
        print("Desligamento automático em 15 minutos")
    else:
        print("Tempo inválido")