'''
Created on May 3, 2012

@authors: Brandon King & Omar Rehmane
'''
from urllib2 import urlopen

class ExampleField(object):
    '''
    ExampleField: This represents a column header (a "cell") in the imaginary spreadsheet.
    '''

    def __init__(self, name, example):
        '''
        name - The name of the field.
        example - A string representation of an individual field from a webpage. 
        '''
        self.name = name
        self.example = example

class ExampleRecord(object):
    '''
    ExampleRecord: This represents a set of fields (a "row") in the imaginary spreadsheet.
    '''
    
    def __init__(self, fields=None):
        '''
        fields - A list of associated ExampleFields.
        '''
        if fields:
            self.fields = fields
        else:
            self.fields = []
    
class ExampleCollection(object):
    '''
    ExampleCollection: This represents the sum total of the scraped data (the entire spreadsheet, as it were) in the imaginary spreadsheet.
    '''
    
    def __init__(self, records=None):
        '''
        records - A list of associated ExampleRecords.
        '''
        if records:
            self.records = records
        else:
            self.records= []

def example_to_DOM(fields, page_url):
    '''
    This method takes in a list of ExampleFields and associates each one with a DOM node from the given page.
    fields - A list of ExampleFields.
    page_url - The URL of the selected page.
    '''
    www = urlopen(page_url)
