"""
This script will download all the dilbert comic strips starting from 16th April 1989

Dilbert Website - dilbert.com
"""

import bs4
import urllib.request
import requests
import datetime
import multiprocessing
import time

def construct_date_list():
    """ Returns a list of dates from 01-01-1989 to current date 
    
    Note: The first Dilbert comics on its website is from 16th April 1989
    """
    start = datetime.datetime.strptime("1989-04-16", "%Y-%m-%d")
    end = datetime.datetime.strptime(datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d"), "%Y-%m-%d")
    
    date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days + 1)]
    
    return date_generated 

def construct_url_list(date_list):
    """ Constructs a set of urls for Dilbert comics

    Urls follow this format - Fixed part - http://dilbert.com/strip
                              Vaiable part - date
    """
    base_url = "http://dilbert.com/strip/"
    url_list = []
    
    for i in date_list:
        temp = base_url + str(i).strip('00:00:00').strip()
        url_list.append(temp)

    return url_list
    
def move_files():
    """ Moves files in yearwise folders """

    pass

f = open('success.txt', 'w')
f2 = open('failed.txt', 'w')


def scraper(url_list):
    """ Put everything together and scrape """
    
    # Scrape
    for i in url_list:
        time.sleep(2)
        try:
            r = requests.get(i)
            c = r.content
            soup = bs4.BeautifulSoup(c, "html.parser")
            tag = soup.find("img", {"class" : "img-comic"})
            link = tag['src']
            filename = i.strip("http://dilbert.com/strip/")
            urllib.request.urlretrieve(link, filename)
            f.write(str(url_list.index(i) + 1))
        except:
            f2.write(str(i.strip("http://dilbert.com/strip/")))



if __name__ == '__main__':
    # Retrieve list of urls
    url_list = construct_url_list(construct_date_list())
    scraper(url_list)
    
    f.close()
    f2.close()
    move_files()
