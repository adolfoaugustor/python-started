frase = "Olá, bem vindo ao treinamento mestres da automação."

print(frase.split())
print(frase.split(","))
print(frase.split("-"))

nomes = "João, Maria, José, Pedro, Ana, Carlos"
print(nomes.split())
print(nomes.split(","))

hashtags = "javascript #python #java #javascript #csharp"
print(hashtags.split())
print(hashtags.split("#"))
print(hashtags.split("#", 3))  # separa apenas os três itens iniciais

separadas_por_virgulas = hashtags.split(" ")
print(separadas_por_virgulas)
print(",".join(separadas_por_virgulas))
print(".".join(separadas_por_virgulas))
print(" ".join(separadas_por_virgulas))
frase1 = "Desafio Manipulação de Strings"
frase2 = "Adolfo,Augusto,Raniley,Kobe"
palavras1 = frase1.split()
print(palavras1)
palavras2 = frase2.split(",")
print(palavras2)
print(",".join(palavras1))
print(" & ".join(palavras2))
