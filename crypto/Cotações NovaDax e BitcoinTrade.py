import requests, json

# Cotações das corretoras: BitcoinTrade, NovaDax
# No final é impresso um dicionário com cotações das duas corretoras, podendo ser utilizados como Json

# Dicionario com cotações
Cotacoes = {}

def bitcointrade():
    lista = {'BTC':'BRLBTC','ETH':'BRLETH','BCH':'BRLBCH','LTC':'BRLLTC','XRP':'BRLXRP','EOS':'BRLEOS','DAI':'BRLDAI'}
    corretora = {'BitcoinTrade':{}}
    
    for i in lista:
        requisicao = requests.get('https://api.bitcointrade.com.br/v3/public/'+lista[i]+'/ticker')
        #print('>>> Crypto:',lista[i],'<<<')
        Symbol = json.loads(requisicao.text)
        Crypto = {i:{'bid':float(Symbol['data']['buy']),'ask':float(Symbol['data']['sell'])}}
        corretora['BitcoinTrade'].update(Crypto)
        #print(Symbol)
    
    #print(corretora)
    Cotacoes.update(corretora)
    

def novadax():
    lista = {'BTC':'BTC_BRL','ETH':'ETH_BRL','BCH':'BCH_BRL','LTC':'LTC_BRL','XRP':'XRP_BRL','EOS':'EOS_BRL','DAI':'DAI_BRL'}
    corretora = {'NovaDax':{}}
    
    for i in lista:
        requisicao = requests.get('https://api.novadax.com/v1/market/ticker?symbol='+lista[i])
        #print('>>> Crypto:',lista[i],'<<<')
        Symbol = json.loads(requisicao.text)
        Crypto = {i:{'bid':float(Symbol['data']['bid']),'ask':float(Symbol['data']['ask'])}}
        corretora['NovaDax'].update(Crypto)
        #print(Symbol)
    
    #print(corretora)
    Cotacoes.update(corretora)
       

#Atualizando todas as cotações
bitcointrade()
novadax()

print(Cotacoes)
