from bs4 import BeautifulSoup

with open("book.xml") as xml_file:
    data = xml_file.read()

soup = BeautifulSoup(data, "lxml-xml")
# print(data)

print(soup.catalog.book.author.text)
print(soup.catalog.book["id"])
print(soup.find("title"))
title = soup("title")

print(title[0].text, title[1].text, title[2].text)

for c in soup.catalog:
    print(c)

# print(type(title))

