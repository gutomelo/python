import ApiNovadax as api
import time
import requests, json
import os

api.Key();

Symbols = api.Tickers()
Symbols_List = []

# Taxa máxima de compra e venda a mercado: 0,30%
# Só posso comprar Bitcoin ou Ethereum
taxa = 0.003
montante = 100.0

def MySymbol(m_symbol, imprime = False):
    Symbol = api.TickerSimbolo(m_symbol)
    if Symbol['code'] == 'A10000' and Symbol['message'] == 'Success':
        if imprime:
            print('Símbolo:',Symbol['data']['symbol'])
            print('Preço Bid:',Symbol['data']['bid'])
            print('Preço Ask:',Symbol['data']['ask'])
    

def MySymbols(imprime = False):
    global Symbols
    global Symbols_List
    Symbols = api.Tickers()
    Symbols_List = []
    
    if Symbols['code'] == 'A10000' and Symbols['message'] == 'Success':
        for i in Symbols['data']:
            Symbols_List.append(i['symbol'])
            if imprime:
                print('Símbolo:',i['symbol'])
        if imprime:
            print(Symbols_List)
            print('Qtd de Símbolos:', len(Symbols_List))
           

def MyTickers(imprime=False):
    global Symbols
    
    tempoi = Symbols['data'][0]['timestamp']
    #Symbols = api.Tickers()
    requisicao = requests.get('https://api.novadax.com/v1/market/tickers')
    Symbols = json.loads(requisicao.text)
    update = (Symbols['data'][0]['timestamp'] - tempoi)/1000
    
    if update > 3:
        print('Tempo de update muito alto, maior que 3!')

    if imprime:
        os.system('clear') or None
        print('*******************************************************')
        for i in Symbols['data']:
            print('Símbolo:',i['symbol'],'Preço Bid:',i['bid'],'Preço Ask:',i['ask'])
        print('Update:',update)
    

os.system('clear') or None
#print(api.Tickers())
#MySimbol('BTC_BRL',True)
#MyTickers(True)
#MySymbols(True)
while True:
    MyTickers(True)
    time.sleep(0.02)           #Tempo maximo de Requisicoes: Publico: 60/s Privado: 20/s


