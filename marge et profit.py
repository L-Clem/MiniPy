import ui
import requests

def calc(sender) :
	pai = v['textfield3'].text
	cou = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=' + pai[0:3] + '&to_currency=' + pai[4:7] + '&apikey=HBX2ARQNYAR083DC'
	ccou = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=EUR&to_currency=' + pai[4:7] + '&apikey=HBX2ARQNYAR083DC'
	res = requests.get(cou)
	ress = requests.get(ccou)
	data = res.json()
	dataa = ress.json()
	c = int(float(data['Realtime Currency Exchange Rate']['5. Exchange Rate']))
	cc = int(float(dataa['Realtime Currency Exchange Rate']['5. Exchange Rate']))
	lev = 1/30
	lo = round((int(v['textfield1'].text)/(c/lev)), 1)
	pip = int(v['textfield2'].text)/(cc*lo)
	v['textview1'].text = str('Il vous faut faire '+ str(pip*1000) + ' pips.')
	sender.title = 'ok'
	
v = ui.load_view('marge et profit')
v.present('sheet')