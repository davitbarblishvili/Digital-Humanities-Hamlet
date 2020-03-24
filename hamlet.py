#!/usr/bin/env python
# coding: utf-8

# # Hamlet
# - Python is very popular in 'Digital Humanities'
# - MIT has the complete works of Shakespeare in a simple [html](http://shakespeare.mit.edu) format
# - an analysis of Hamlet by reading the html file, one line at 
# a time and doing pattern matching
# - The goal is to return (the linecnt, total number of 'speeches', dict)
# where the dict shows the number of 'speeches' each character gives
# 

# # Serving Hamlet
#     - to start it, evaluate the cell below 
#     - once it is running, [this page](http://localhost:8123/hamlet.html) should display Hamlet
#     - if you want to kill the server, do Kernel/Restart in the networking file

# In[ ]:


import sys
import http.server
import socketserver
sys.platform

port = 8123

# url = http://localhost:8002

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", port), Handler)

print("serving at port", port)
httpd.serve_forever()


# In[ ]:


# must eval this cell

import urllib.request
import collections
import re
import bs4
import lxml

# location of hamlet web page

hamleturl = 'http://localhost:8123/hamlet.html'


# In[ ]:


# show first 40 lines of hamlet file

with urllib.request.urlopen(hamleturl) as ef:
    for j in range(40):
        print(next(ef))


# In[ ]:


# order of key/value pairs is arbitrary
from collections import defaultdict
import re

def hamlet():
    ham_dict = defaultdict(int)
    line_count = 0 
    speech_count = 0
    speech_arr = []
    pat = 'NAME=speech'
    with urllib.request.urlopen(hamleturl) as rd:
        for line in rd.readlines():
            if len(re.findall(pat,line.decode())) != 0:
                speech_count += 1
                clean_speech = re.compile('<.*?>')
                speech_arr.append((re.sub(clean_speech, '', line.decode())).rstrip())
            line_count += 1
    ham_dict = {i:speech_arr.count(i) for i in speech_arr}  
    return line_count,speech_count,ham_dict
 
hamlet()


# In[ ]:




