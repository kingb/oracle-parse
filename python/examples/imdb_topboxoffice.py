# -*- coding: utf-8 -*-
import pprint

from oracleparse import example
from oracleparse import oracle

record = example.ExampleRecord([])
record.add_field('rank', "10")
record.add_field('movie', "Think Like a Man (2012)")
record.add_field('weekend', "$8.11M")
record.add_field('gross', "$73.1M")
record.add_field('weeks', "4")

sybil = oracle.Oracle(record, 'http://www.imdb.com/chart/')
data = sybil.parse(strip=True)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data)
