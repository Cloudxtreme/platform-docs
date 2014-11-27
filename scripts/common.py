#!/usr/bin/python
import html2text
from lxml import etree
import os

h = html2text.HTML2Text()

scriptspath = os.path.dirname(os.path.realpath(__file__))

#xslt_tree = etree.parse("confluence2markdown.xsl")
xslt_tree = etree.parse(scriptspath + "/confluence2xhtml.xsl")
transform = etree.XSLT(xslt_tree)

def convertToMarkdown(page):
    # Wrap Confluence XML in headers and such
    strWrapperTop = "<?xml version=\"1.0\"?>" \
        "<!DOCTYPE ac:confluence SYSTEM \"confluence-all.dtd\" [ " \
        "<!ENTITY clubs    \"&#9827;\">" \
        "<!ENTITY nbsp   \"&#160;\">" \
        "<!ENTITY ndash   \"&#8211;\">" \
        "<!ENTITY mdash   \"&#8212;\">" \
        "<!ENTITY rsquo   \"&#8217;\">" \
        "<!ENTITY lsquo   \"&#8216;\">" \
        " ]>" \
        "<ac:confluence xmlns:ac=\"http://www.atlassian.com/schema/confluence/4/ac/\" xmlns:ri=\"http://www.atlassian.com/schema/confluence/4/ri/\" xmlns=\"http://www.atlassian.com/schema/confluence/4/\">"
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
