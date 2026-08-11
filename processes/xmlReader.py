from collections import OrderedDict
from typing import Any

import xmltodict


def read_XML(file_name: str) -> OrderedDict[str, Any]:
    """Reads *.xml file and parses data in dictionary

    Params:
        file_name (str): Path leading to *.xml file with input data.

    Returns:
        OrderedDict: Required data in dictionary
    """
    data = {}

    with open(file_name, "r", encoding="utf-8") as f:
        data = xmltodict.parse(f.read())

    return data
