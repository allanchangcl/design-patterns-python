from xml.etree.ElementTree import ElementTree
import unittest
from factory_pattern import connector


class TestConnector(unittest.TestCase):
    def setUp(self):
        pass

    def test_connector_json(self):
        jsondata = connector.connection_factory("factory_pattern/data/donut.json")
        # print(jsondata.parsed_data)
        assert isinstance(jsondata.parsed_data[0], dict)

    def test_connector_xml(self):
        xmldata = connector.connection_factory("factory_pattern/data/person.xml")
        # print(xmldata.parsed_data)
        assert isinstance(xmldata.parsed_data, ElementTree)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
