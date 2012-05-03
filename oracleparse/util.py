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


def node_to_absolute_XPATH(node):
    """
    Returns an absolute XPATH for a node
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
