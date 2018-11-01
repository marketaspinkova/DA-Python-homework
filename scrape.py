"""
from requests_html import HTML
soubor = open('sample.html', encoding="utf-8")
obsah = soubor.read()
soubor.close()
scraper = HTML(html=obsah)

print(scraper.find("p"))

for odst in scraper.find("p"):
	print(odst.text)

for znacka in scraper.find("a"):
	print(znacka.text)
	print(znacka.attrs["href"])

for znacka in scraper.find("ul li"):
	print(znacka.text)

for znacka in scraper.find(".sekce1"):
	print(znacka.text)
"""
"""
# stahovani z internetu_____________________________________________________________________________

from requests_html import HTMLSession
session = HTMLSession()
stranka = session.get('http://scrape.kodim.cz/sample/index')
for odstavec in stranka.html.find('p'):
  print(odstavec.text)

for znacka in stranka.html.find("li"):
	print(znacka.text)
	"""

"""
from requests_html import HTMLSession
session = HTMLSession()
stranka = session.get('http://scrape.kodim.cz/dhmo/index')

for znacka in stranka.html.find('h2'):
  print(znacka.text)

for znacka in stranka.html.find("a"):
  print(znacka.attrs["href"])

for znacka in stranka.html.find('img'):
  print(znacka.attrs["src"])
"""


from requests_html import HTMLSession
session = HTMLSession()
stranka = session.get('http://kodim.cz/kurzy/python-data/')

kapitoly = []
for znacka in stranka.html.find('h3'):
  kapitoly.append(znacka.text)
odkazy = []
for znacka in stranka.html.find('a'):
  odkazy.append(znacka.attrs["href"])

soubor = open("chapters.csv", "w")
[soubor.write(kapitoly[x] + "\t" + odkazy[x] + "\n") for x in range(len(kapitoly))]
soubor.close()


stranka.html.render(sleep=5)
print(stranka.html.html)


	
