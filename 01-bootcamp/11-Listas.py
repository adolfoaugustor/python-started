# Listas

site1 = "youtube.com"
site2 = "facebook.com"
site3 = "instagram.com"

sites = ["youtube.com", "facebook.com", "instagram.com"]
print(sites[1])
sites.append("twitter.com")
print(sites)
sites.remove("facebook.com")
print(sites)

# Listas dinâmicas
pessoas = [["Adolfo", 35], ["Maria", 25]]
print(pessoas[0][0])
print(pessoas[1][1])

objetos = ["monitor", "teclado", "mouse"]
print(objetos)
# adicionar um valor a cada objeto, sendo nome e valor
objetos[0] = ["monitor", 500]
objetos[1] = ["teclado", 100]
objetos[2] = ["mouse", 50]
print(objetos)
