import pprint

from oracleparse import example
from oracleparse import oracle

record = example.ExampleRecord([])
#record.example = """012    Freedom Al-Anon    
#Union Church    Mon 6:00pm
#200 Prospect Street    Open; Wayside Rm #204
#Berea, KY 40403"""

record.add_field("district", "012")
record.add_field("meeting_name", "Freedom Al-Anon")
record.add_field("location", "Union Church")
record.add_field("address", "200 Prospect Street")
record.add_field("city", "Berea")
record.add_field("day/time", "Mon 6:00pm")
record.add_field("day/time2", "Mon, Wed, Fri 6:30pm")
record.add_field("info", "Open; Wayside Rm #204")
record.add_field("info2", "meet in basement")

sybil = oracle.Oracle(record, 'http://www.kyal-anon.org/alalist12.html')
data = sybil.parse(strip=True)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data)
