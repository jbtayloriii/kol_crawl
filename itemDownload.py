#!usr/bin/python

import argparse
import sys
import urllib2
from HTMLParser import HTMLParser
import re

itemhtmlre = re.compile(r'<div id="description".*</blockquote><script type="text/javascript">', re.DOTALL)

def main():
	domain = ''
	parser = argparse.ArgumentParser(description='downloads kol item information')
	parser.add_argument('-d', '--domain', help='domain to use (gotta be logged in)')
	args = parser.parse_args()
	domain = args.domain

	test = downloadItem(domain, 408549054);
	print(test)

def downloadItem(domain, itemId):
	url = "{0}/desc_item.php?whichitem={1}".format(domain, itemId);
	response = urllib2.urlopen(url)

	html = response.read().strip()

	parser = ItemHTMLParser()
	parser.feed(html)
	matches = itemhtmlre.findall(html)
	if len(matches) > 0:
		itemid = parser.itemid
		return (itemid, matches[0])
	return None

class ItemHTMLParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.shouldPrint = 0;
		self.itemid = -1


	def handle_starttag(self, tag, attrs):
		if tag == "div":
			if self.shouldPrint > 0:
				self.shouldPrint += 1
			else:
				for attr in attrs:
					if attr[0] == "id" and attr[1] == "description":
						self.shouldPrint += 1

	def handle_endtag(self, tag):
		if tag == "div" and self.shouldPrint > 0:
			self.shouldPrint -= 1

	def handle_data(self, data):
		if self.shouldPrint > 0:
			pass
			#print(data)

	def handle_comment(self, data):
		if 'itemid' in data:
			itemgroup = re.findall('\d+', data)
			if len(itemgroup) > 0:
				self.itemid = int(itemgroup[0])
				print(self.itemid)


if __name__ == '__main__':
	main()
