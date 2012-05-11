"""
Created on May 3, 2012

@authors: Brandon King & Omar Rehmane
"""
from util import url_to_DOM, text_filter_strip_newline, node_to_absolute_XPATH, DEFAULT_USER_AGENT
from disambiguation import take_last

class ExampleField(object):
    """
    This represents a column header (a "cell") in the imaginary spreadsheet.
    """

    def __init__(self, name, example):
        """
        name: The name of the field.
        example: A string representation of an individual field from a webpage. 
        """
        self.name = name
        self.example = example
        self.xpath = None

class ExampleRecord(object):
    """
    This represents a set of fields (a "row") in the imaginary spreadsheet.
    """

    def __init__(self, fields=None):
        """
        fields: A list of associated ExampleFields.
        """
        if fields:
            self.fields = fields
        else:
            self.fields = []

    def add_field(self, name, example):
        field = ExampleField(name, example)
        self.fields.append(field)


class ExampleCollection(object):
    """
    This represents the sum total of the scraped data (the entire spreadsheet, as it were) in the imaginary spreadsheet.
    """

    def __init__(self, records=None):
        """
        records: A list of associated ExampleRecords.
        """
        if records:
            self.records = records
        else:
            self.records = []

def example_to_node(field, page_url, filter=False, disambiguation_method=take_last,
                    text_filter_func=text_filter_strip_newline):
    """
    This method takes in an ExampleField and finds the target node that contains that example.
    field: An ExampleField.
    page_url: The URL of the selected page.
    filter: If text_filter_func shold be applied to text before comparison.
    disambiguation_method: This should be a method that takes in a list and somehow decides which node to return.
    text_filter_func: Allows the user to supply a function for filtering text.
        default: util.text_filter_strip_newline (removes surrounding whitespace and replaces newlines with ''
    """
    root = url_to_DOM(page_url)
    if filter:
        target_nodes = [ node for node in root.iterdescendants() if text_filter_func(node.text_content()) == text_filter_func(field.example) ]
    else:
        target_nodes = [ node for node in root.iterdescendants() if node.text_content() == field.example ]
    if len(target_nodes) == 0:
        raise ValueError('Node containing the given example not found. Field(%s)' % (field.name))
    else:
        return disambiguation_method(target_nodes)

def examples_to_nodes(field_list, page_url, text_filter_func=text_filter_strip_newline, user_agent=DEFAULT_USER_AGENT):
    """
    For each field, set the selected node.
    """
    root = url_to_DOM(page_url, user_agent)
    d = {}
    for field in field_list:
        target_nodes = [ node for node in root.iterdescendants() \
                        if text_filter_func(node.text_content()) == text_filter_func(field.example) ]

        d[field.name] = []
        for node in target_nodes:
            xpath = node_to_absolute_XPATH(node)
            record_count = len(root.findall(xpath))
            d[field.name].append((node, xpath, record_count))

    return d

def node_selection(field_list, url, user_agent=DEFAULT_USER_AGENT):
    d = examples_to_nodes(field_list, url, user_agent=user_agent)

    d_xpath_count = {}
    d_count = {}

    # Set up helper dictionaries for discriminating selection choices
    for key in d:
        d_xpath_count[key] = set([ (n[1], n[2]) for n in d[key] ])
        d_count[key] = set([ n[2] for n in d[key] ])

    # Process intersections
    xpath_count_set = None
    count_set = None
    for key in d:

        # Skip the first set, since there is nothing to intersect it with
        if xpath_count_set is None:
            xpath_count_set = d_xpath_count[key]
            count_set = d_count[key]
            continue

        # Calculate intersections of sets
        xpath_count_set = xpath_count_set.intersection(d_xpath_count[key])
        count_set = count_set.intersection(d_count[key])

    print("NODE SELECTION:")
    print("  xpath_count_set_intersection: %d" % (len(xpath_count_set)))
    print("  count_set_intersect: %d" % (len(count_set)))
    print("")
    for xpath, count in xpath_count_set:
        print("  XPath(%s) Hits: %s" % (xpath, count))
    for count in count_set:
        print("  Count Hits: %s" % (count))


    # We found a full disambiguation set most likely
    if len(xpath_count_set) == 1:
        rd = {}
        target = xpath_count_set.pop()
        for key in d:
            rd[key] = [ n for n in d[key] if n[1] == target[0] and n[2] == target[1] ]
        return rd

    # We found a matching count (no ambiguity)
    elif len(count_set) == 1:
        rd = {}
        target = count_set.pop()
        for key in d_xpath_count:
            rd[key] = [ n for n in d[key] if n[2] == target]
            #if len(rd[key]) > 1:
            #    raise ValueError("Not sure how to handle multiple matches: %s (key: %s)" % (rd, key))
        return rd

    # Multiple disambiguation sets
    elif len(xpath_count_set) > 1:
        raise ValueError("Node selection: Multiple disambiguation matches not implemented")
    # Multiple non-ambiguous matchs
    elif len(count_set) > 1:
        raise ValueError("Node selection: Multiple non-ambiguous matches not implemented")
    else:
        raise ValueError("Node selection: No matches found across all fields")



