import webbrowser
import threading
import time
import random

def comentar(site, comentario):
   if site == 8:
      raise Exception("Erro ao comentar no site")
   print(f"Entrando no site: {site}")
   print(f"Comentando: {comentario}")
   time.sleep(1)
   print(f"Dados Processados no site: {site}")

comentarios = [
   "Ótimo site",
   "Muito bom",
   "Gostei muito",
   "Recomendo",
   "Não gostei",
   "Péssimo"
]
threads = []
for site in range(10):
   nova_thread = threading.Thread(
      target=comentar, 
      args=(site, random.choice(comentarios)))
   threads.append(nova_thread)

for thread in threads:
   thread.start()

for thread in threads:
   thread.join()