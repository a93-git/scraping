""" Scrape all the Garfield comic strips """

from datetime import date, timedelta
from urllib.request import urlretrieve
from multiprocessing.pool import ThreadPool
from time import time as timer
import os
from time import sleep

base_url = "https://d1ejxu6vysztl5.cloudfront.net/comics/garfield/"

# Calculate days from the 1st day to today
d1 = date(1978, 6, 19)  # start date
d2 = date.today()  # end date

delta = d2 - d1         # timedelta

# Get the dates
datelist = [] 
for i in range(delta.days + 1):
    datelist.append((d1 + timedelta(days=i)))

# Create urls
url_list = []
for i in datelist:
    url_list.append(base_url + str(i.year) + "/" + str(i) + ".gif")

print(len(url_list))

# Grab urls
def get_comic(i):
    """ Takes in a url and retrieves the comic from that url
    Return: Returns a tuple of url, and error"""
    filename = i[-14:]
    try:
        urlretrieve(i, filename)
        return None, None
    except Exception as e:
        return i, e

start = timer()

# Map the get_comic function over each element of url_list list
results = ThreadPool(40).imap_unordered(get_comic, url_list)

for url, error in results:
    if error is None:
        pass
    else:
        print("Error in fetching %r: %s" %(url, error))

print("Elapsed time: %s" %(timer() - start,))
