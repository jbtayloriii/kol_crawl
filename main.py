#!usr/bin/python

import argparse
import displayCollectionParse
import itemDownload

def main():
	domain = ''
	parser = argparse.ArgumentParser(description="takes display case items in holderofsecret's display case and does a lookup on them. NOTE: this will make a lot of http GET requests, be careful")
	parser.add_argument('-d', '--domain', help='domain logged into kol')
	args = parser.parse_args()
	domain = args.domain

	playerid = 216194 #HolderOfSecret's id, we use this because they're the one with the most unique collectibles
	itemidlist = displayCollectionParse.getItemIdListFromDisplayCase(domain, playerid)
	for x in xrange(20):
		itemid = itemidlist[x]
		texttuple = itemDownload.downloadItem(domain, itemid)
		if texttuple is None:
			print("Could not get item " + str(itemid))
			return
		realid = texttuple[0]
		text = texttuple[1]
		f = open('item_' + str(realid)+ '.txt', 'w')
		f.write(text)
		f.close()

if __name__ == '__main__':
	main()
