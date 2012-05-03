from lxml.html import soupparser
from urllib2 import urlopen

def url_to_DOM(url):
    """
    url: url to html,
    
    returns DOM of html
    """
    www = urlopen(url)
    html = www.read()

    return soupparser.fromstring(html)
