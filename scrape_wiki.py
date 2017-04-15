import requests
import pandas as pd
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = 'https://en.wikipedia.org/wiki/List_of_gairaigo_and_wasei-eigo_terms'
    session = requests.Session()
    page = session.get(url).text
    soup = BeautifulSoup(page, 'lxml')

    rows = soup.find_all('tr')
    get_cells = lambda row: row.find_all('td')
    is_valid_row = lambda cells: len(cells) == 5
    filtered_rows = filter(is_valid_row, map(get_cells, rows))

    flashcard = {'front': [], 'back': []}
    for cells in filtered_rows:
        flashcard['front'].append(cells[0].text)
        flashcard['back'] .append(cells[2].text)
    df = pd.DataFrame(flashcard)
    df = df[['front', 'back']]
    df.to_csv('katakana_flashcards.csv', index=False, header=False)
