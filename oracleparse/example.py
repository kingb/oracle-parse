"""
Created on May 3, 2012

@authors: Brandon King & Omar Rehmane
"""
from util import url_to_DOM
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
            self.records= []

def example_to_node(field, page_url, strip=False, disambiguation_method=take_last):
    """
    This method takes in an ExampleField and finds the target node that contains that example.
    field: An ExampleField.
    page_url: The URL of the selected page.
    strip: If whitespace should be stripped from the end of the html and the example.
    disambiguation_method: This should be a method that takes in a list and somehow decides which node to return.
    """
    root = url_to_DOM(page_url)
    if strip:
        target_nodes = [ node for node in root.iterdescendants() if node.text_content().strip() == field.example.strip() ]
    else:
        target_nodes = [ node for node in root.iterdescendants() if node.text_content() == field.example ]
    if len(target_nodes) == 0:
        raise ValueError('Node containing the given example not found.')
    else:
        return disambiguation_method(target_nodes)
    