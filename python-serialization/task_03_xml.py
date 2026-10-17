import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """make to XML file"""

    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    ET.indent(tree, space=" ")
    tree.write(filename, encoding="unicode", xml_declaration=False)


def deserialize_from_xml(filename):
    """make to JSON format"""

    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}
    for child in root:
        result[child.tag] = child.text

    return result
