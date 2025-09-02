import xmltodict
from typing import OrderedDict, Any


def read_XML(file_name: str) -> OrderedDict[str, Any]:
    data = {}

    with open(file_name, "r", encoding="utf-8") as f:
        data = xmltodict.parse(f.read())
    
    return data


def main() -> None:
    read_XML("elektronicky_formular_xml.xml")


if __name__ == "__main__":
    main()