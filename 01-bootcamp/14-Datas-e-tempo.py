# Datas e tempo
from datetime import datetime

# print(datetime.now())
# print(datetime.now().day)
# print(datetime.now().month)
# print(datetime.now().year)

# print(datetime(2022,12,22))
# postar_a_foto = input('Quando devemos postar a foto (dd/mm/yyyy)? ')
# print(datetime.strptime(postar_a_foto, '%d/%m/%Y'))

data_inicio = datetime.now()
data_final = datetime(2025, 9, 24)

print(data_final - data_inicio)
