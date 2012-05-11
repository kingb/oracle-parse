# -*- coding: utf-8 -*-
import pprint

from oracleparse import example
from oracleparse import oracle

record = example.ExampleRecord([])
record.add_field('title', "ESA Declares Flagship Envisat Observing Satellite Lost")
record.add_field('abstract', u"""An anonymous reader writes with news that the European Space Agency has lost contact with its Envisat environmental satellite mere weeks after celebrating a full decade in orbit. Engineers have spent the last month trying to re-establish contact, and will continue to do so for another two months. "With ten sophisticated sensors, Envisat has observed and monitored Earth’s land, atmosphere, oceans and ice caps during its ten-year lifetime, delivering over a thousand terabytes of data. An estimated 2500 scientific publications so far have been based on this information, furthering our knowledge of the planet." The ESA was hoping Envisat would stay operational for another two years, until Sentinel satellites from the Global Monitoring for Environment and Security initiative became operational.""")

sybil = oracle.Oracle(record, 'http://slashdot.org/')
data = sybil.parse(strip=True)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data)
