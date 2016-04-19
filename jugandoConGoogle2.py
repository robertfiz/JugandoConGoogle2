#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    The MIT License (MIT)

    Copyright (c) 2016 sinfonier-project

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
"""

import sys,StringIO, urllib, urllib2, cgi, re, socket
from urlparse import urlparse
import basesinfonierspout
import json

import basesinfonierbolt

class JugandoConGoogle2(basesinfonierbolt.BaseSinfonierBolt):
      
    def __init__(self):

        basesinfonierbolt.BaseSinfonierBolt().__init__()

    def userprepare(self):

        # TO-DO: Init values. Code here runs once

        self.variable = "hello"

        # Get Param (get value of "param_name" from input box)
        self.name = self.getParam("param_name")

    def userprocess(self):
    	url = 'https://www.google.com/xhtml?'		
	q = 'site:'+str(sys.argv[1])
	start=0
	num=100
	gws_rd = 'ssl'
	query_string = { 'q':q, 'start':start, 'num':num, 'gws_rd':gws_rd }
	data = urllib.urlencode(query_string)
	url = url + data
	headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)', 'Referer' : 'http://127.0.0.1/'} # $
	try:
        	req = urllib2.Request(url, None, headers)
                google_reply = urllib2.urlopen(req).read()
                regex = '<h3 class="r"><a href="/url(.+?)">'
                pattern = re.compile(regex)
                url_links = re.findall(pattern, google_reply)
        except urllib2.URLError:
                pass

	hosts=[]
	ips=[]
	
	for url in url_links:
		url2=url.strip('?q=')
		try:
			d=urlparse(url2)
			if d.netloc not in hosts:
				hosts.append(d.netloc)	
                except socket.error:
                        pass


        for host in hosts:
        	self.addField(host)
	   	self.emit()
               
JugandoConGoogle2().run()







    def usernextTuple(self):
        for host in hosts:
            
            try:
                st = self.it.next().split(",")
                self.addField(host)

                self.emit()

            except StopIteration:
                pass

JugandoConGoole().run()
