from bs4 import BeautifulSoup
import requests

def parse_url(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    start = soup.find(name="p")
    text = ""
    for element in start.next_elements:
        if element.name == 'p':
            text += element.text
    return text