from oracleparse import util, example

class Oracle(object):
    """
    "Whenever you don't know how to solve a problem, ask the oracle."
    ~Prof. Ras Bodik, UC Berkeley (from CS164: Hack Your Language!)
    """
    def __init__(self, record, url):
        """
        record: An ExampleRecord object that contains the fields we're interested in.
        url: The URL of the page we're interested in.
        """
        self.example_record = record
        self.url = url
        
    # TODO methods we need
    # method to disambiguate between fields in case of Xpath collision
    
    def parse(self):
        fields = self.example_record.fields
        
        records = []
        
        start_field = fields[0]
        
        root = util.url_to_DOM(self.url)
        
        target_node = example.example_to_node(start_field, self.url)
        datapath = util.node_to_absolute_XPATH(target_node)
        
        start_data = root.findall(datapath)
        
        for datum in start_data:
            records.append({start_field.name: datum.text})
        
        # parse the DOM for each field and store the data
        for field in fields[1:]:
            target_node = example.example_to_node(field, self.url)
            datapath = util.node_to_absolute_XPATH(target_node)
        
            data = root.findall(datapath)
            
            for index in range(len(data)):
                records[index][field.name] = data[index].text
        
        return records
