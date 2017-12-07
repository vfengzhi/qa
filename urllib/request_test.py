#coding=utf-8
import urllib
import urllib2
import httplib
import cookielib
import sys
import requests
from bs4 import BeautifulSoup
import json

def usingGet(url):
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	the_page=response.read()
	#print the_page
	return the_page


def usingPost(url,data):
	'''
	data={
        'key1':'value1',
        'key2':'value2'
	}
	'''
	post_data=urllib.urlencode(data)

	req=urllib2.Request(url,post_data)
	response = urllib2.urlopen(req)
	the_page = response.read()
    #print the_page
	return the_page

def getWithCookie(url):
	'''
	build a new opener !!
	return opener and turn to other page with it 
	'''
	cookie = cookielib.CookieJar()
	handler=urllib2.HTTPCookieProcessor(cookie)
	opener = urllib2.build_opener(handler)
	response = opener.open(url)      
	the_page=response.read()
	# print the_page
	return opener

def postWithCookie(url ,data):
	'''
	For login validation,
	and turn to other pages with login information
	'''
	data={
		'username':'myname',
		'password':'mypasswd'
	}

	post_data=urllib.urlencode(data)

	cookie = cookielib.CookieJar()
	handler=urllib2.HTTPCookieProcessor(cookie)
	opener = urllib2.build_opener(handler)

	req=urllib2.Request(url,post_data)
	response = opener.open(req)
	the_page = response.read()

def bs(the_page):
	html = BeautifulSoup(the_page,'lxml')

	attr_name = ''
	attr_value = ''
	tag = html.findAll(tagname,{attr_name:attr_value})[0]

	# foreach get every tag
	# for t in tag :
	# 	print t
	
	key = ''
	value = tag.attrs[key]
	return 






