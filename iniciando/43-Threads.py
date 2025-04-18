import webbrowser
import threading
import time


def extrair_dados_site(site):
   print(f"Estamos navegando até o site: {site}")
   webbrowser.open(site)
   for i in range(1, 20):
      print(f"processando dados {i}/19")
      time.sleep(1)
   print(f"Finalizando a de dados do site")

def baixar_arquivos():
   for i in range(10):
      print(f"Baixando arquivo {i}/10")
      time.sleep(1)
   print(f"Finalizando o download dos arquivos")

nova_thread = threading.Thread(
   target=extrair_dados_site, 
   args=("https://www.devaprender.com",), daemon=True)
nova_thread.start()
nova_thread.join()
baixar_arquivos()