#classe

class computador:
    def __init__(self, marca, memoria_ram, placa_de_video, hd):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
        self.hd = hd

    def Ligar(self):
        print('Estou ligando o computador')

    def Desligar(self):
        print('Estou desligando o computador')

    def ExibirInformacoes(self):
        print(self.marca, self.memoria_ram, self.placa_de_video, self.hd)

computador1 = computador('PHILCO', '8GB', 'NVIDIA', '1TB')
computador1.Ligar()
computador1.ExibirInformacoes()
computador1.Desligar()
