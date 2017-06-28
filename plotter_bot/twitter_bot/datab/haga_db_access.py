from xml.dom import minidom
xmldoc = minidom.parse('haga_db.xml')
itemlist = xmldoc.getElementsByTagName('item')
print(len(itemlist)) #Menge der Elemente

for s in itemlist:
    print(s.attributes['tweets'].value) #value der Elemente printen
