# Import Statements
import requests
from bs4 import BeautifulSoup

# Get the Request from the URL
request = requests.get('https://londoncocktailweek.com/bars/print/?collectionId=0&whatId=0&areaId=0&spiritId=0&openNow=0&search=')

# Parse the request
all_bars = BeautifulSoup(request.text, 'html.parser')
bars = all_bars.select('.bar_name')
soup = BeautifulSoup(request.text, 'html.parser')

# finding parent <ul> tag
parent = soup.find("ul")
  
# finding all <li> tags
text = list(parent.descendants)

ul = soup.find('ul')
children = ul.findChildren("li", recursive=False)
bars = []
addresses = []
descriptions = []
for i, child in enumerate(children):
    bar = child.find('h2', {"class": "bar_name"}).getText()
    address = child.find('div', {'class': 'text'}).getText()
    opening_hours_container = child.find('ul', {'class': 'opening_hours__container'})
    opening_hours = opening_hours_container.find_all('li', {'class': 'opening_hours__times'})
    for day in opening_hours:
        day_of_week = day.find('div', {'class': 'text'}).getText()
        hours = day.find('li', {'class': 'text'}).getText()
    description = child.find('p', {'class': 'text--padded'}).getText()
    bars.append(bar)
    addresses.append(address)
    descriptions.append(description)

b = []
for i, item in enumerate(bars):
    title = item.getText()
    b.append(title)

print(b)