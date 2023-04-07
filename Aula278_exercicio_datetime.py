from datetime import datetime

from dateutil.relativedelta import relativedelta

emprestimo = 1000000
anos_emprestimo = 5
valor_parcela = emprestimo / (anos_emprestimo * 12)

data_inicial = datetime.strptime('2020-12-20', '%Y-%m-%d')
data_final = data_inicial

for month in range(anos_emprestimo * 12):
    data_final += relativedelta(months=+1)
    print(
        f'DATA:{data_final.strftime("%Y/%m/%d")} Parcela: R$ {valor_parcela:,.2f}')

utlima_data = data_final.strftime("%Y/%m/%d")
