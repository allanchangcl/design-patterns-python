# import json
import unittest
from factory_pattern import json_connector


class TestJsonConnector(unittest.TestCase):
    def setUp(self):
        pass

    def test_json_connector(self):
        parsed = json_connector.JSONConnector("factory_pattern/data/donut.json")
        # print(parsed.parsed_data)
        # print(parsed.parsed_data(parsed, indent=4, sort_keys=True))
        # testdict = dict()
        # print(isinstance(parsed.parsed_data[0], dict))
        # print(isinstance(testdict, dict))
        assert isinstance(parsed.parsed_data[0], dict)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
