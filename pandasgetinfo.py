import pandas as pd 
import datetime as date

df = pd.read_excel(r"/home/nick/Desktop/Developing/Projects/SAEBot/Assets/SpreadSheet/CONTROLE ANAC SAE. RVB 2021 .xlsx")  # r = reads path
total_linhas = df.shape[0]
# print(total_linhas)
# print(df.loc[1])
# linha_1 = df.loc[0]
# print(linha_1, ['CIF'])


check_date_user_input = input("Insira a data do check (dd/mm/aaaa): ")
check_date_user_input = check_date_user_input.split("/")
check_date_user_input_dia = int(check_date_user_input[0])
check_date_user_input_mes = int(check_date_user_input[1])
check_date_user_input_ano = int(check_date_user_input[2])


def compare_check_date(check_date, date_compare):
    return (check_date == date_compare)

# if compare_check_date(df.loc[0, 'DATA CHECK'], date.datetime(2021, 1, 20)):
#     print("As datas são iguais")

numero_registros = 0

for x in range(0, total_linhas):
    if compare_check_date(df.loc[x, 'DATA CHECK'], date.datetime(check_date_user_input_ano, check_date_user_input_mes, check_date_user_input_dia)):
        print("As datas são iguais na linha", x+1)
        numero_registros+=1

if numero_registros == 0:
    print("Nenhum registro encontrado.")
