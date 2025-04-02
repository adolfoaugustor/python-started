class EmailDeBoasVindas:
   def __init__(self):
      self.pessoas = ['João', 'Maria', 'Pedro', 'Ana', 'Lucas']

   def Iniciar(self):
      print('Iniciando o envio de emails...')
      emails_apresentacao = self.MontarCredencial(self.pessoas)
      for email in emails_apresentacao:
         print(email)

   def MontarCredencial(self, pessoas):
      credenciais = []
      for pessoa in pessoas:
         credenciais.append(f'Olá {pessoa}, seja bem-vindo!')
      return credenciais

email = EmailDeBoasVindas()
email.Iniciar()

# Teste de Debugging
# F5 inicia a debugger
# F10 analisa a linha sem entrar no codigo interno
# F11 entra no codigo interno 
# Shift+F11 sai do codigo interno e continua a execução