#!/usr/bin/python

import threading
import listparser as lp
import requests
import re
import feedparser as fp

threadcount = 0
threadarray=[]



def getrss( path ):
	response = requests.get(path)
	return response.content
	
def processrss ( indata ):
	links = fp.parse(indata)
	return links
	
	
class myThread (threading.Thread):
	def __init__(self, url, threadid):
		threading.Thread.__init__(self)
		self.url = url
		self.threadid = threadid
		
	def run(self):
		rssdata = getrss(self.url)
		setoflinks = processrss(rssdata)
		#print self.threadid 
		for post in setoflinks.entries:
			output = str(self.threadid) + ": " + setoflinks['feed']['title'] + ": " + post.title + ": " + post.link + "\n"		
			
			udata = output.decode("utf-8")
			print udata.encode("ascii","ignore")			




subs = lp.parse('/home/trev/dev/python/youtube/subscription_manager')


for url in range(0, len(subs.feeds)):
	threadarray.append("")
	nonssladd = re.sub(r"https:", "http:", subs.feeds[url].url)
	threadarray[threadcount] = myThread(nonssladd, threadcount)
	threadarray[threadcount].start()
	threadcount += 1
	

