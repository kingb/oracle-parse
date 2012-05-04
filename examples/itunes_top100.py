from oracleparse import example
from oracleparse import oracle

field1 = example.ExampleField('song-title', 'Call Me Maybe')
field2 = example.ExampleField('album-title', 'Gotye')

record = example.ExampleRecord([field1, field2])

sybil = oracle.Oracle(record, 'http://www.apple.com/itunes/charts/songs/')
print sybil.parse()
