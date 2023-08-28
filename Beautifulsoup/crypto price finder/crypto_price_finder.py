from bs4 import BeautifulSoup
import requests

url = 'https://coinmarketcap.com/'
result = requests.get(url).text
doc = BeautifulSoup(result, 'html.parser')


# prices dictionary
prices = {}

# finding table data
tbody = doc.tbody

# find table rows
trs = tbody.contents

# looping through the top 10 rows
for tr in trs[:10]:
	name = tr.contents[2]
	price = tr.contents[3]

	true_name = name.p.string
	true_price = price.a.string

	prices[true_name] = true_price
print(prices)
