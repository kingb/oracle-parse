from oracleparse import util, example, disambiguation

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

    def parse(self, strip=False, index_tags=util.INDEXED_TAGS, disambiguate_func=disambiguation.take_last,
              user_agent=util.DEFAULT_USER_AGENT):
        fields = self.example_record.fields

        # PASS 0: Select Nodes
        selected_nodes = example.node_selection(fields, self.url, user_agent=user_agent)
        for field in fields:
            node, xpath, count = disambiguate_func(selected_nodes[field.name])
            field.node = node
            field.xpath = xpath

        # PASS 1: Cross-field XPath disambiguation
        self._disambiguate(strip, index_tags)


        # PASS 2: Collect up selected data
        records = []
        start_field = fields[0]

        root = util.url_to_DOM(self.url)

        #target_node = example.example_to_node(start_field, self.url, strip)
        #datapath = util.node_to_absolute_XPATH(target_node)

        start_data = root.findall(start_field.xpath)
        print "Field (start): %s" % (start_field.name)
        print "  XPath: %s" % (start_field.xpath)
        print "  Data Count: %d" % (len(start_data))

        for datum in start_data:
            records.append({start_field.name: datum.text_content()})


        # parse the DOM for each field and store the data
        for field in fields[1:]:
            target_node = example.example_to_node(field, self.url, strip)
            #datapath = util.node_to_absolute_XPATH(target_node)

            data = root.findall(field.xpath)

            print "Field: %s" % (field.name)
            print "  XPath: %s" % (field.xpath)
            print "  Data Count: %d" % (len(data))

            for index in range(len(data)):
                records[index][field.name] = data[index].text_content()

        return records

    def _disambiguate(self, strip, index_tags):
        """
        Updates field.xpath with disambiguiated xpath.
        
        returns None
        """
        fields = self.example_record.fields

        disambig = {}
        for field in fields:
            #field.node = example.example_to_node(field, self.url, strip)
            #field.xpath = util.node_to_absolute_XPATH(field.node, index_tags)
            disambig.setdefault(field.xpath, []).append(field)

        for xpath, field_list in disambig.items():
            assert len(field_list) > 0

            # Disambiguate if there is more than one field with the same xpath
            if len(field_list) > 1:
                ref_field = field_list[0]
                for other_field in field_list[1:]:
                    ref_xpath, other_xpath = util.disambiguate_xpath(ref_field.node, other_field.node, index_tags)
                    other_field.xpath = other_xpath
                    ref_field.xpath = ref_xpath
            # Only one field, therefore we know the xpath is unique

