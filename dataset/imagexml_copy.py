import xml.etree.ElementTree as ET

root = ET.Element("name")
root.text="drug1"

for i  in range(1, 1000):
    dataListFile = "Drugxml/drug"+str(i)+".xml"
    ET.ElementTree(root).write(dataListFile, "utf-8")