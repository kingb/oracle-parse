import pprint

from oracleparse import example
from oracleparse import oracle

record = example.ExampleRecord([])
record.add_field('City', 'Seattle Al-Anon')
record.add_field('Day', 'Sun')
record.add_field('Time', '8:30 AM')
record.add_field('Location', """4101 15th Ave NE
UW School of Social Work 
Entrance corner of 41st and 15th - take elevator to 3rd 
Room 305 second on left.""")
record.add_field('Meeting Name', 'Sunday AM Fresh Start AFG (Open)')
record.add_field('District', '20')

sybil = oracle.Oracle(record, 'http://www.wa-al-anon.org/Meeting-Seattle-All.html')
data = sybil.parse(strip=True)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data)
