#!/usr/bin/python
import html2text
from lxml import etree
import os, re

# Should really share this somehow..
from Wiki import *
wiki = Wiki()

h = html2text.HTML2Text()

scriptspath = os.path.dirname(os.path.realpath(__file__))

#xslt_tree = etree.parse("confluence2markdown.xsl")
xslt_tree = etree.parse(scriptspath + "/confluence2xhtml.xsl")
transform = etree.XSLT(xslt_tree)

# Convert the page content XML to HTML then to markdown
def convertXMLToMarkdown(page):
    # Wrap Confluence XML in headers and such
    strWrapperTop = """<?xml version="1.0" ?>
        <!DOCTYPE ac:confluence SYSTEM "confluence-all.dtd" [
        <!ENTITY clubs  "&#9827;">
        <!ENTITY nbsp   "&#160;">
        <!-- # Grabbed a bunch from http://www.w3.org/TR/html4/sgml/entities.html#misc -->
        <!ENTITY quot    "&#34;">
        <!ENTITY amp     "&#38;">
        <!ENTITY lt      "&#60;">
        <!ENTITY gt      "&#62;">
        <!ENTITY OElig   "&#338;">
        <!ENTITY oelig   "&#339;">
        <!ENTITY circ    "&#710;">
        <!ENTITY tilde   "&#732;">
        <!ENTITY ensp    "&#8194;">
        <!ENTITY emsp    "&#8195;">
        <!ENTITY thinsp  "&#8201;">
        <!ENTITY zwnj    "&#8204;">
        <!ENTITY zwj     "&#8205;">
        <!ENTITY lrm     "&#8206;">
        <!ENTITY rlm     "&#8207;">
        <!ENTITY ndash   "&#8211;">
        <!ENTITY mdash   "&#8212;">
        <!ENTITY lsquo   "&#8216;">
        <!ENTITY rsquo   "&#8217;">
        <!ENTITY sbquo   "&#8218;">
        <!ENTITY ldquo   "&#8220;">
        <!ENTITY rdquo   "&#8221;">
        <!ENTITY bdquo   "&#8222;">
        <!ENTITY dagger  "&#8224;">
        <!ENTITY Dagger  "&#8225;">
        <!ENTITY permil  "&#8240;">
        <!ENTITY lsaquo  "&#8249;">
        <!ENTITY rsaquo  "&#8250;">
        <!ENTITY euro   "&#8364;">
        ]>
        <ac:confluence xmlns:ac="http://www.atlassian.com/schema/confluence/4/ac/" xmlns:ri="http://www.atlassian.com/schema/confluence/4/ri/" xmlns="http://www.atlassian.com/schema/confluence/4/">
        """
    strWrapperBottom = "</ac:confluence>"
    strConfluenceXMLDoc = strWrapperTop + page['content'] + strWrapperBottom

    try:
        doc = etree.fromstring(strConfluenceXMLDoc)
        result = transform(doc)
    except ValueError:
        print "Error converting Confluence XML"
        print "Raw XML input:"
        print page['content']
        raise

    return "# " + page['title'] + "\n\n" + h.handle(unicode(result).encode("ascii","ignore"))

# Get rendered content then convert to markdown
def convertToMarkdown(page):
    result = wiki.server.confluence2.renderContent(wiki.token, page['space'], page['id'], '', {"style" : "clean"})
    # Hack to replace syntaxhighlighter macro with vanilla code blocks
    result = re.sub(r'<script type="syntaxhighlighter".*?><!\[CDATA\[(.*?)\]\]></script>', r'<pre>\1</pre>', result, flags=re.DOTALL)
    return "# " + page['title'] + "\n\n" + h.handle(unicode(result).encode("ascii","ignore"))


