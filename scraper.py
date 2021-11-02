# Import Statements
from bs4 import BeautifulSoup
import pandas as pd
import requests
from datetime import datetime

# Create the Data Frame with Columns
df = pd.DataFrame(columns=[
    'Bar Name',
    'Address',
    'Description',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
])

# Get the Request from the URL
request = requests.get(
    'https://londoncocktailweek.com/bars/print/?collectionId=0&whatId=0&areaId=0&spiritId=0&openNow=0&search='
)

# Parse the request using Beautiful Soup
soup = BeautifulSoup(request.text, 'html.parser')

# Find all the bar list items
bar_list = soup.find('ul')
bars = bar_list.findChildren("li", recursive=False)

# Loop throught the bars
for i, bar in enumerate(bars):

    # Get the name, address and description
    bar_name = bar.find('h2', {'class': 'bar_name'}).getText()
    address = bar.find('div', {'class': 'text'}).getText()
    description = bar.find('p', {'class': 'text--padded'}).getText()

    # Get the opening hours
    opening_hours_container = bar.find(
        'ul', {'class': 'opening_hours__container'}
    )
    weekly_opening_hours = opening_hours_container.find_all(
        'li', {'class': 'opening_hours__times'}
    )

    # Loop through the opening hours and store in an array
    times = []
    for opening_hours in weekly_opening_hours:
        day_of_week = opening_hours.find('div', {'class': 'text'}).getText()
        hours = opening_hours.find('li', {'class': 'text'}).getText()
        times.append(hours)

    # Add the data to a data-frame
    df.loc[i] = [
        bar_name,
        address,
        description,
        times[0],
        times[1],
        times[2],
        times[3],
        times[4],
        times[5],
        times[6]
    ]
csv_string = 'bar_csvs/bar_list_' + datetime.now().strftime("%Y_%m_%d_%H-%M-%S") + '.csv'
df.to_csv(csv_string)
