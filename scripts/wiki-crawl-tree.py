#!/usr/bin/env python
from Wiki import *
from common import *
import os, re

wiki = Wiki()

h = html2text.HTML2Text()

def cleanTitle(value):
    value = re.sub(r'[^\w\s-]', r'-', value).strip().lower()
    value = re.sub('[-\s]+', '-', value)
    return value

# Fetch children for a page and recurse
def fetchChildren(page, prefix=''):
    print prefix + '/' + cleanTitle(page['title'])

    # Load the full page
    fullpage = wiki.server.confluence2.getPage(wiki.token, page['id'])
    # Convert it to markdown
    markdown = convertToMarkdown(fullpage)
    # Save the markdown
    f = open(prefix + '/' + cleanTitle(page['title']) + '.md', 'w+')
    f.write(markdown)
    f.close()

    # Append title to prefix and process children
    prefix = prefix + '/' + cleanTitle(page['title'])
    children = wiki.server.confluence2.getChildren(wiki.token, page['id'])
    if (len(children) > 0):
        if not os.path.isdir(prefix):
            os.mkdir(prefix)
        for child in children:
            fetchChildren(child, prefix)

if len(sys.argv) < 3:
    exit("Usage: " + sys.argv[0] + " spacekey pagetitle")

spacekey = sys.argv[1]
pagetitle = sys.argv[2]

page = wiki.server.confluence2.getPage(wiki.token, spacekey, pagetitle)
if page is None:
    exit("Could not find page " + spacekey + ":" + pagetitle)

fetchChildren(page, os.getcwd())
