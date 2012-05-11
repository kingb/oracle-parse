# -*- coding: utf-8 -*-
import pprint

from oracleparse import example
from oracleparse import oracle

record = example.ExampleRecord([])
#record.add_field('title', "USPS To Ban International Shipping On Lithium Ion Powered Gadgetry")
record.add_field("abstract", '''"Apparently the USPS is enacting a ban on the international shipment of all devices containing Lithium Ion batteries. The ban is expected to lift in January of 2013. It seems like this would drive more business away from the already floundering USPS financial situation. The article focuses on the shipment of items out of the U.S., but doesn't mention whether the same ban will apply to purchasing these items on eBay from overseas sources."''')

sybil = oracle.Oracle(record, 'http://slashdot.org/')
data = sybil.parse(strip=True)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data)
