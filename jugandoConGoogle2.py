import sys,StringIO, urllib, urllib2, cgi, re, socket
from urlparse import urlparse
import basesinfonierspout
import json

class JugandoConGoogle2(basesinfonierbolt.BaseSinfonierBolt):
	def __init__(self):
		basesinfonierbolt.BaseSinfonierBolt().__init__()

	def userprepare(self):
		self.hostname = self.getParam("hostname")
		self.h=self.getField(self.hostname)
    		self.url = 'https://www.google.com/xhtml?'		
		self.q = 'site:'+h
		self.start=0
		self.num=100
		self.gws_rd = 'ssl'
		self.query_string = { 'q':q, 'start':self.start, 'num':self.num, 'gws_rd':self.gws_rd }
		self.data = urllib.urlencode(self.query_string)
		self.url = self.url + self.data
		self.headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)', 'Referer' : 'http://127.0.0.1/'} # $
		try:
        		self.req = urllib2.Request(self.url, None, self.headers)
                	self.google_reply = urllib2.urlopen(req).read()
                	self.regex = '<h3 class="r"><a href="/url(.+?)">'
                	self.pattern = re.compile(regex)
                	self.url_links = re.findall(pattern, google_reply)
        	except urllib2.URLError:
                	pass

		self.hosts=[]
		self.ips=[]
		

    	def userprocess(self):
    	
	
		for self.url in self.url_links:
			self.url2=url.strip('?q=')
			try:
				self.d=urlparse(sel.url2)
				if self.d.netloc not in self.hosts:
					self.hosts.append(self.d.netloc)	
                	except socket.error:
                        	pass


        	for self.host in self.hosts:
        		self.addField(json.dumps(self.host))
	   	self.emit()
               
JugandoConGoogle2().run()




