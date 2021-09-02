#!/bin/python3

"""
Function that gets specific countries through a substring name and greater than a population number.
"""
import sys
import os
import urllib.request
import json


# Complete the function below.
# https://jsonmock.hackerrank.com/api/countries/search?name=
def  getCountries(s, p):
    content = req_countries(s, 1)
    # print(content)
    counter = 0

    pages = content['total_pages']

    for page in range(2, pages+1):
        content = req_countries(s, page)
        for country in content['data']:
            print(country['name'])
            print(country['population'])
            if country['population'] > p:
                counter+=1
    print(counter)

def req_countries(s, page):
    url = 'https://jsonmock.hackerrank.com/api/countries/search?name=' + s.lower() + '&page=' + str(page)
    request = urllib.request.Request(url)

    r = urllib.request.urlopen(request).read()
    return(json.loads(r.decode('utf-8')))


res = getCountries('in', 1000000)

