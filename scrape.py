import requests
from bs4 import BeautifulSoup

def get_soup(url):
    session = requests.Session()
    page = session.get(url).text
    soup = BeautifulSoup(page, 'lxml')
    return soup

def filter_rows(soup, filter_fn):
    rows = soup.find_all('tr')
    get_cells = lambda row: row.find_all('td')
    filtered = filter(filter_fn, map(get_cells, rows))
    return filtered
