import json, requests, time, os, vlc

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

# Data
url = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'

limit = 19500
risk = 30

while True:

	# Get the coin price
	response = requests.get(url).text
	value = json.loads(response)
	actual_price = float(value['price'])
	print('BTC price', actual_price)
	print('--------------------')

	# Risk management
	percents = [0.010, 0.015, 0.020, 0.025, 0.03]
	for per in percents:
		amount = risk / per
		pos = truncate(amount / actual_price, 3)
		print('Pos. Size', per, ':', pos)

	if actual_price > limit:
		p = vlc.MediaPlayer("Watchout.mp3")
		p.play()
		time.sleep(30)

	# Go to sleep
	print('\n')
	time.sleep(2)
	