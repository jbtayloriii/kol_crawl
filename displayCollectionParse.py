#!usr/bin/python

import argparse
import sys
import urllib2
from urllib2 import Request, urlopen, URLError
from HTMLParser import HTMLParser

#216194

def main():
	domain = ''
	parser = argparse.ArgumentParser(description='gets a list of item ids from a display case. (you should be logged in for this to work)')
	parser.add_argument('-d', '--domain', help='domain to use (gotta be logged in)')
	parser.add_argument('-p', '--player', help='player id')
	args = parser.parse_args()
	domain = args.domain
	playerId = args.player
	getItemIdListFromDisplayCase(domain, playerId)

def getItemIdListFromDisplayCase(domain, playerId):
	url = "{0}/displaycollection.php?who={1}".format(domain, playerId);
	try:
		response = urllib2.urlopen(url)
		html = response.read()
		parser = displayCaseHTMLParser()
		parser.feed(html)

		return parser.itemIdList

		#print(parser.itemIdList)
		#print("Count: " + str(len(parser.itemIdList)))
		#print(html)
	except URLError as e:
		if hasattr(e, 'reason'):
			print 'We failed to reach a server.'
			print 'Reason: ', e.reason
		elif hasattr(e, 'code'):
			print 'The server couldn\'t fulfill the request.'
			print 'Error code: ', e.code

class displayCaseHTMLParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.itemIdList = []


	def handle_starttag(self, tag, attrs):
		if tag == 'img':
			for attr in attrs:
				if attr[0] == 'onclick' and attr[1].startswith('descitem('):
					textsplit1 = attr[1].split('descitem(', 1)[1]
					itemId = textsplit1.split(',', 1)[0]
					self.itemIdList.append(int(itemId))

if __name__ == '__main__':
	main()
