import unittest
from factory_pattern import xml_connector


class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_xml_connector(self):
        parsed = xml_connector.XMLConnector("factory_pattern/data/person.xml")
        # print(parsed.parsed_data)
        liars = parsed.parsed_data.findall(
            ".//{}[{}='{}']".format("person", "lastName", "Liar")
        )
        # print(liars[0][1].text)
        # print("found: {} persons".format(len(liars)))
        assert len(liars) == 2

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
