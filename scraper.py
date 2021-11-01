# Import Statements
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Create the inital Data Frame
df = pd.DataFrame(columns=['Bar Name', 'Address', 'Description', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

# Get the Request from the URL
request = requests.get('https://londoncocktailweek.com/bars/print/?collectionId=0&whatId=0&areaId=0&spiritId=0&openNow=0&search=')

# Parse the request
soup = BeautifulSoup(request.text, 'html.parser')

ul = soup.find('ul')
children = ul.findChildren("li", recursive=False)
for i, child in enumerate(children):
    bar = child.find('h2', {"class": "bar_name"}).getText()
    address = child.find('div', {'class': 'text'}).getText()
    opening_hours_container = child.find('ul', {'class': 'opening_hours__container'})
    opening_hours = opening_hours_container.find_all('li', {'class': 'opening_hours__times'})
    times = []
    for day in opening_hours:
        day_of_week = day.find('div', {'class': 'text'}).getText()
        hours = day.find('li', {'class': 'text'}).getText()
    description = child.find('p', {'class': 'text--padded'}).getText()
        times.append({j: hours})
    
    
    # Add the data to a data-frame
    df.loc[i] = [bar, address, description, times[0], times[1], times[2], times[3], times[4], times[5], times[6]]
