#!/usr/bin/python3

import requests, bs4

#baseUrl = 'https://pro-football-reference.com/teams'

#Download the desired webpage - use ARZ 'crd' as a test for now
response = requests.get('https://pro-football-reference.com/teams/crd/2022.htm')

#Condition that kills program if status code is !200
response.raise_for_status()

#Create a bs4 object from the downloaded webpage
soup = bs4.BeautifulSoup(response.text, 'html.parser')

#Scrape the CSV file for W/R/T and QB

#Right now this recognizes the table and picks it up as a bs4 result set, but does not scrape any data. Returns a length of 0.
wrt_csv = soup.select('table #rushing_and_receiving > tr > td')
print(type(wrt_csv))

#qb_csv = soup.select('TO_DO: get csv table for qb attribute')


#Verify the csv was correctly scraped
print(str(wrt_csv))
#print(str(qb_csv))
