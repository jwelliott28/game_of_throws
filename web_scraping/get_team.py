#!/usr/bin/python3

import requests


#Create a web page object
res = requests.get('https://www.pro-football-reference.com/teams/kan/2022.htm')

#Print the status code to make sure it was retrieved successfully
print(res.status_code)
