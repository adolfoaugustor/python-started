# heranca
class Computador:
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

class Notebook(Computador):
    def __init__(self, marca, memoria_ram, placa_de_video, hd, cor_led):
        self.cor_led = cor_led
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
        self.hd = hd

    def exibir_informacoes(self):
        print(self.marca, self.memoria_ram, self.placa_de_video, self.hd, self.cor_led)

    def trocar_cor_led(self, cor):
        print(f'Cor do LED alterada para {cor}')
    
    def ligar_ventoinha(self):
        print('Ventoinha ligada')

    def desligar_ventoinha(self):
        print('Ventoinha desligada')

notebook = Notebook('Dell', '16GB', 'GTX 1050', '1TB', 'vermelho')
notebook.Ligar()
notebook.ExibirInformacoes()
notebook.trocar_cor_led('azul')
notebook.ligar_ventoinha()
notebook.desligar_ventoinha()
notebook.Desligar()