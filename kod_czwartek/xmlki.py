import xml.dom.minidom

doc = xml.dom.minidom.parse("../book.xml")

print(doc.nodeName)
print(doc.firstChild.tagName)

new = doc.createElement("book")
new.setAttribute("id", "bk999")
doc.firstChild.appendChild(new)

book = doc.getElementsByTagName("book")
author = doc.getElementsByTagName("author")
print(f"ilość książek: {book.length}")
for i in book:
    print(i.getAttribute("id"))

print(f"Autorzy: {author.length}")
for i in author:
    print(i.childNodes[0])

# with open("book2.xml", "w") as f:
#     f.write(str(doc))

