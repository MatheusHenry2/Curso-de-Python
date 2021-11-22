from datetime import date, datetime
today = date.today()

dia = int(input('Informe o dia do nascimento :'))
mes = int(input('Informe o mês do nascimento'))
ano = int(input('Informe o ano do nascimento'))

if today.year - ano < 18:
    print(f'Você ainda vai se alistar no exercito sua idade é {today.year - ano} anos')
elif today.year - ano == 18:
    print(f'já é hora de se alistar no exercito sua idade é {today.year - ano} anos')
else:
    print(f'já passou da hora né cara sua idade é {today.year - ano} anos')




