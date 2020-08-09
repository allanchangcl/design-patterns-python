from factory_pattern import json_connector
from factory_pattern import xml_connector


# factory method
def connection_factory(filepath):
    if filepath.endswith("json"):
        connector = json_connector.JSONConnector
    elif filepath.endswith("xml"):
        connector = xml_connector.XMLConnector
    else:
        raise ValueError("Cannot connect to {}".format(filepath))
    return connector(filepath)
