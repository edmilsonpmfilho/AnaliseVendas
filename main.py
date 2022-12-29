import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console - Acrescente aqui seu sid do twilio
account_sid = ""
# Your Auth Token from twilio.com/console - Acrescente aqui seu Token do twilio
auth_token = ""
client = Client(account_sid, auth_token)



lista_meses =['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'Encontrou no mês de {mes}, alguém bateu a meta. Vendedor {vendedor} e as Vendar foram de {vendas}')
        message = client.messages.create(
            #Adicione aqui o numero que para o qual deseja enviar o SMS
            to="",
            #Adicione aqui o seu numero criado pelo twileo
            from_="",
            body=f'Encontrou no mês de {mes}, alguém bateu a meta. Vendedor {vendedor} e as Vendar foram de {vendas}')

        print(message.sid)







