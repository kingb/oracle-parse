import pprint

from oracleparse import example
from oracleparse import oracle

record = example.ExampleRecord()
record.add_field('song-title', 'Call Me Maybe')
record.add_field('artist', 'Gotye')


sybil = oracle.Oracle(record, 'http://www.apple.com/itunes/charts/songs/')
data = sybil.parse()

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data)
