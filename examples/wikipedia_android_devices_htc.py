# -*- coding: utf-8 -*-
import pprint

from oracleparse import example
from oracleparse import oracle

record = example.ExampleRecord([])

record.add_field("name", "beTouch E110")
record.add_field("release_date", "February 15, 2010")
#record.add_field("version", "1.5")
#record.add_field("display", u"3.2 in (81 mm), 320×480 HVGA, portrait mode")
#record.add_field("inputs", "A-GPS")
#record.add_field("networks", "GSM/GPRS/EDGE 850 900, 1800 1900 HSDPA")
#record.add_field("connectivity", """Wi-Fi 802.11b/g
#Bluetooth 2.1 with A2DP stereo and EDR
#FM tuner
#3.5 mm stereo audio jack, micro-USB""")
#record.add_field("CPU/GPU/CHIPSET", "600 MSM7227")
#record.add_field("capabilities", "576 MB RAM, 512 MB ROM, about 140 MB usable")
#record.add_field("camera(s)", "Rear: 5 Mpx Front: none")
#record.add_field("notes", "A mid-range AT&T exclusive; similar to HTC Legend")


sybil = oracle.Oracle(record, 'http://en.wikipedia.org/wiki/Comparison_of_Android_devices')
data = sybil.parse(strip=True)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data)
