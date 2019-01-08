import xml.dom.minidom

dom = xml.dom.minidom.parse("Exemmelle.xml")

xml = dom.toprettyxml()
print(xml)

