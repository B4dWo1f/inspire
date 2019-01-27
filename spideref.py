#!/usr/bin/python3
# -*- coding: UTF-8 -*-


from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


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
   print('$ python spideref.py http://inspirehep.net/record/1495568/references')
   exit()

if url[-1] == '/': url = url[:-1]

f_out = url.split('/')[-2] + '.bib'
url_root = 'http://inspirehep.net'

html_doc = make_request(url)
S = BeautifulSoup(html_doc, 'html.parser')
inside = S.find('div',class_='inside')
table = inside.find('table')

## Get links to all the referenced papers
print('Getting the links from the referenced papers...')
links = []
for link in table.find_all('a'):
   try: link['class']
   except KeyError:
      links.append( url_root+''.join(link['href'].split()) )
print('  ... %s papers retrieved'%(len(links)))

## Get links to the bibtex for each paper
print('Get links to the bibtex for each paper...')
links_bib = []
for l in links:
   html_doc = make_request(l)
   Sl = BeautifulSoup(html_doc,'html.parser')
   for link in Sl.find_all('a'):
      try:
         if 'export/hx' in link['href']:
            links_bib.append(url_root+link['href'])
         else:pass
      except: pass
print('  ... %s bibtex links retrieved'%(len(links_bib)))

## Download the bibtex references
print('saving to: %s'%(f_out))
f = open(f_out,'w')
bibs = []
for lb in links_bib:
   html_doc = make_request(lb)
   Slb = BeautifulSoup(html_doc,'html.parser')
   bib = Slb.find('pre')
   f.write(bib.text+'\n')
   f.flush()
f.close()
