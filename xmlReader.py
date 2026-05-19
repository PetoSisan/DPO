import xmltodict
from typing import OrderedDict, Any


def read_XML(file_name: str) -> OrderedDict[str, Any]:
    """Reads *.xml file and parses data in dictionary

    Args:
        file_name: Path leading to *.xml file with input data.
    
    Returns:
        Required data in dictionary
    """
    data = {}

    with open(file_name, "r", encoding="utf-8") as f:
        data = xmltodict.parse(f.read())
    
    return data