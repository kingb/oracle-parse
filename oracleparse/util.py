from lxml.html import soupparser
from urllib2 import urlopen

def url_to_DOM(url):
    """
    Returns the DOM of the HTML at the given URL.
    url: url of the page we're interested in.
    """
    www = urlopen(url)
    html = www.read()

    return soupparser.fromstring(html)


def node_to_absolute_XPATH(node):
    """
    Returns an absolute XPATH for a given DOM node.
    node: The target node whose absolute XPATH we want.
    """
    def helper(node, current_list):
        if current_list is None:
            current_list = []

        parent = node.getparent()
        if parent is None or parent.tag.lower() == 'html':
            current_list.append(node.tag)
            return current_list

        current_list.append(node.tag)
        return helper(parent, current_list)

    xpath = helper(node, [])
    xpath.reverse()
    xpath = '/'.join(xpath)
    return xpath
