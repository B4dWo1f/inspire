#!/usr/bin/python3
# -*- coding: UTF-8 -*-




import os
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


def make_request(url):
   """ Make http request """
   req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
   html_doc = urlopen(req)
   html_doc = html_doc.read().decode(html_doc.headers.get_content_charset())
   return html_doc


import sys
try: url = sys.argv[1]
except IndexError:
   print('URL not specified')
   print('Usage example:')
   print('$ python mybibtex.py "http://inspirehep.net/search?ln=en&ln=en&p=exactauthor%3AJ.Doe.1&of=hb&action_search=Search&sf=earliestdate&so=d&rm=&rg=250&sc=0"')
   print('*Notice the quotes in the url to avoid problems with special characters')
   exit()
if url[-1] == '/': url = url[:-1]


f_out = 'mypapers.bib'

html_doc = make_request(url)
S = BeautifulSoup(html_doc, 'html.parser')
table_row = S.select("table.searchresultsbox tr")[0]
Nresults = table_row.findAll('td')[1].text
Nresults = int(Nresults.split()[0])
papers = []
for link in S.find_all('a'):
   try:
      if 'export/hx' in link['href']:
         papers.append(link['href'])
   except: pass
## Manual warnig
if len(papers) < Nresults:
   print('WARNING: Scraping through multiple result pages is not implemented yet, try setting the number of results shown to a bigger number.')
   print('Alternatively, you can manually re-run the program with each of the results pages and append each of the resulting bib\'s')

print('saving to: %s'%(f_out))
f = open(f_out,'w')
bibs = []
for l in papers:
   html_doc = make_request(l)
   Slb = BeautifulSoup(html_doc,'html.parser')
   bib = Slb.find('pre').text
   bib = bib.strip()
   f.write(bib+'\n\n')
   f.flush()
f.close()

