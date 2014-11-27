#!/usr/bin/env python
from Wiki import *
import html2text
from lxml import etree
import os
from pprint import pprint

wiki = Wiki()

h = html2text.HTML2Text()

if len(sys.argv) < 3:
   exit("Usage: " + sys.argv[0] + " spacekey pagetitle")

spacekey = sys.argv[1]
pagetitle = sys.argv[2]

page = wiki.server.confluence2.getPage(wiki.token, spacekey, pagetitle)
if page is None:
   exit("Could not find page " + spacekey + ":" + pagetitle)

#pprint(page)
print(page['title'])

def fetchChildren(parent, gparenttitle=''):
  children = wiki.server.confluence2.getChildren(wiki.token, parent['id'])
  for page in children:
    print gparenttitle + ';' + parent['title'] + ';' + page['title']
    fetchChildren(page, parent['title'])

fetchChildren(page)
