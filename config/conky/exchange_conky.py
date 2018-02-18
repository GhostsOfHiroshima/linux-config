#!/bin/python2.7


OUTPUT_FILE_USD = '/home/icebox/.config/conky/usd.txt'
OUTPUT_FILE_EURO = '/home/icebox/.config/conky/euro.txt'
UPDATE_EVERY = 60 			# x minutes

import requests as req
from lxml import html
from time import gmtime, strftime

def update():
	print 'updating ...'
	r = req.get('http://www.cursbnr.ro/', headers={'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0'})
	tree = html.fromstring(r.text)
	
	euro = tree.xpath('//div[@class="currency-value"]/div[@class="value"]')[0].text.encode('utf-8')
	usd = tree.xpath('//div[@class="currency-value"]/div[@class="value"]')[1].text.encode('utf-8')
	
	with open(OUTPUT_FILE_USD, 'w') as f:
		f.write(usd)
	with open(OUTPUT_FILE_EURO, 'w') as f:
		f.write(euro)
	
	print strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
	print usd
	print euro
	print '---------------------------'
	
def main():
	from time import sleep
	while True:
		update()
		sleep(UPDATE_EVERY * 60)
	
if __name__ == "__main__":
	main()
