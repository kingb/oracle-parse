'''
Created on May 3, 2012

@authors: Brandon King & Omar Rehmane
'''

class ExampleField(object):
    '''
    ExampleField: This represents a column header (a "cell") in the imaginary spreadsheet.
    '''

    def __init__(self, example):
        '''
        Constructor
        '''
        self.example = example

class ExampleRecord(object):
    '''
    ExampleRecord: This represents a set of fields (a "row") in the imaginary spreadsheet.
    '''
    def __init__(self):
        pass
    
class ExampleCollection(object):
    '''
    ExampleCollection: This represents the sum total of the scraped data (the entire spreadsheet, as it were) in the imaginary spreadsheet.
    '''
    def __init__(self):
        pass
