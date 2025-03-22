estilos_musicais = ['rock', 'jazz', 'blues', 'pop', 'reggae']
# for estilo in estilos_musicais:
#     if estilo == 'blues':
#         print(estilo.upper())

# for estilo in estilos_musicais:
#     if estilo == 'blues':
#         break
#     print(estilo.upper())


for estilo in estilos_musicais:
    if estilo == 'blues':
        continue
    print(estilo.upper())
