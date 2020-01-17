#!/usr/bin/env python

from urllib2 import Request, urlopen, URLError, HTTPError

index = (r"""
_____ _   _ ____ _____ _____ _     _____
|_   _| | | |  _ \_   _|_   _| |   | ____|
  | | | | | | |_) || |   | | | |   |  _|
  | | | |_| |  _ < | |   | | | |___| |___
  |_|  \___/|_| \_\|_|   |_| |_____|_____|

Codado Por Monius
Exemplo: site.com.br
""")

try:
    from colorama import Fore as F
except:
	print (index)
	print ("[!] Install: pip install colorama")
	exit()

print (F.GREEN + index + F.RESET)

def findAdmin():
	f = open("list.txt","r");
	link = raw_input(" \nInsira a URL: ")
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "Painel Encontrado: ",req_link

findAdmin()
