import pprint

from oracleparse import example
from oracleparse import oracle

record = example.ExampleRecord([])
record.add_field('town', 'Auburn')
record.add_field('location', 'United Methodist Church of Auburn')
record.add_field('address', '439 Park Avenue')
record.add_field('time', '7:30 P.M.')

sybil = oracle.Oracle(record, 'https://sites.google.com/a/maineafg.org/ais/Monday-Meetings')
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(sybil.parse(strip=True))
