from lxml.html import soupparser
from urllib2 import urlopen

INDEXED_TAGS = ['table']

def url_to_DOM(url):
    """
    Returns the DOM of the HTML at the given URL.
    url: url of the page we're interested in.
    """
    www = urlopen(url)
    html = www.read()

    return soupparser.fromstring(html)


def node_to_absolute_XPATH(node, index_tags=INDEXED_TAGS):
    """
    Returns an absolute XPATH for a given DOM node.
    node: The target node whose absolute XPATH we want.
    """
    def helper(node, current_list, force_absolute=False):
        if current_list is None:
            current_list = []

        parent = node.getparent()
        if parent is None or parent.tag.lower() == 'html':
            current_list.insert(0, node.tag)
            return

        #force recording of index into xpath based on tag
        if node.tag in index_tags or force_absolute:
            current_list.insert(0, node.tag + '[%d]' % (get_xpath_index(node)))
            force_absolute = True
        else:
            current_list.insert(0, node.tag)
        helper(parent, current_list, force_absolute)
        return

    xpath_list = []
    helper(node, xpath_list)
    xpath = '/'.join(xpath_list)
    return xpath

def disambiguate_xpath(node1, node2, index_tags=INDEXED_TAGS):

    def helper(node1, node1_list, node2, node2_list, done_flag=False, force_absolute=False):
#        if node1_list is None:
#            node1_list = []
#            node2_list = []

        parent1 = node1.getparent()
        parent2 = node2.getparent()

        if parent1 is None or parent1.tag.lower() == 'html':
            node1_list.insert(0, node1.tag)
            node2_list.insert(0, node2.tag)
            return

        index1 = get_xpath_index(node1)
        index2 = get_xpath_index(node2)

        # found difference, can disambiguate
        if (index1 != index2 and not done_flag) or str(node1.tag).lower() in index_tags or force_absolute:
            node1_list.insert(0, node1.tag + '[%d]' % (int(index1)))
            node2_list.insert(0, node2.tag + '[%d]' % (int(index2)))
            done_flag = True
            if str(node1.tag).lower() in index_tags:
                force_absolute = True
        else:
            node1_list.insert(0, node1.tag)
            node2_list.insert(0, node2.tag)

        helper(parent1, node1_list, parent2, node2_list, done_flag, force_absolute)
        return

    node1_list = []
    node2_list = []
    helper(node1, node1_list, node2, node2_list)
    #print node1_list
    #print node2_list
    xpath1 = '/'.join(node1_list)
    xpath2 = '/'.join(node2_list)
    #print xpath1
    #print xpath2
    return (xpath1, xpath2)


def get_xpath_index(node):
    parent = node.getparent()
    if parent is None:
        raise ValueError("Node(%s) has no parent" % (node.tag))

    children = parent.getchildren()
    # filter for only the same tags
    children = [ child for child in children if child.tag == node.tag ]

    #return the xpath index
    return children.index(node) + 1


def text_filter_strip_newline(text):
    """
    text_filter function:
     * strips trailing/leading whitespace
     * removes newline characters.
    """
    def no_double_whitespace(text):
        """
        All spaces should be a single space
        """
        prev_len = len(text)
        cur_len = -1
        while prev_len != cur_len:
            prev_len = len(text)
            text = text.replace('  ', ' ')
            cur_len = len(text)

        return text

    return no_double_whitespace(text.strip().replace('\r\n', ' ').replace('\n', ' ').replace('\r', ' '))
