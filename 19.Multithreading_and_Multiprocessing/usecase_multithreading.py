'''
Real world example: multithreading for I/O bound tasks
Scenario: Web Scrapping
Web Scrapping often invloves making numerous network requests to fetch webpages.
These tasks these tasks are I/O bound because they spend a lot of time waiting for responses 
from servers. Multithreading can significantly improve the performance by allowing multiple
web pages to be fetched concurrently.
'''

import threading
import requests
from bs4 import BeautifulSoup

urls=[
    'https://python.langchain.com/v0.2/docs/introduction/',
    'https://python.langchain.com/v0.2/docs/concepts/',
    'https://python.langchain.com/v0.2/docs/tutorials/'
]

def fetch_contents(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f'Fetched {len(soup.text)} charcaters from {url}')

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_contents, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All Web Pages Fetched")


"""
Explanation of args=(url,):
args is a tuple: The args parameter expects a tuple of arguments, even if there's only one argument to pass.
args=(url,): This creates a tuple with a single element url. The comma is necessary to define it as a tuple.
If you write args=(url), it would be interpreted as just url, not a tuple. Without the comma, it would lead 
to an error or unexpected behavior because the function would not receive its arguments correctly.
"""









