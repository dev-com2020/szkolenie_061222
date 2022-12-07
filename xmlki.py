from xml.dom.minidom import parse, parseString, Node

# document = parse("dane.svg")

with open("dane.svg") as file:
    document = parse(file)


def set_id_attribute(parent, attribute_name="id"):
    if parent.nodeType == Node.ELEMENT_NODE:
        if parent.hasAttribute(attribute_name):
            parent.setIdAttribute(attribute_name)
        for child in parent.childNodes:
            set_id_attribute(child, attribute_name)


set_id_attribute(document)
print(document.getElementById("skin"))

