'''
Vamos imaginar que você vai criar uma classe chamada NavegadorDeSites,
essa classe terá 2 propriedades, uma chamada "site" e outra chamada "propriedades".
A classe tambem tera um método chamado acessar_site, esse método deverá simplesmente imprimir
para qual site está navegando e quais informações será extraida, com base nas infromações que foram passadas
no construtor. Ex: Navegando até o site devmedia.com.br para extrair quantidade de postagens
feitas até hoje.
'''
class NavegadorDeSites:
    def __init__(self, site, conteudo_a_buscar):
        self.site = site
        self.conteudo_a_buscar = conteudo_a_buscar

    def acessar_site(self):
        print(f"Navegando até o site {self.site} para extrair {self.conteudo_a_buscar}.")


class NavegadorDeSitesDeComparacao(NavegadorDeSites):
    def buscador_de_preco(self, nome_do_produto, preco):
        print(
            f"Buscando o preço do produto {nome_do_produto} no site {preco}.")

# Exemplo de uso:
navegador = NavegadorDeSitesDeComparacao("http://olx.com.br", "Camaro 2021")
navegador.acessar_site()
navegador.buscador_de_preco("Camaro 2021", 100000)