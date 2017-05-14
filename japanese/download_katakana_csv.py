import pandas as pd

from anki_scrape import scrape

if __name__ == '__main__':
    url = 'https://en.wikipedia.org/wiki/List_of_gairaigo_and_wasei-eigo_terms'
    soup = scrape.get_soup(url)

    is_valid_row = lambda cells: len(cells) == 5
    filtered_rows = scrape.filter_rows(soup, is_valid_row)

    flashcard = {'front': [], 'back': []}
    for cells in filtered_rows:
        katakana = cells[0].text
        flashcard['front'].append(katakana)
        origin = cells[2].text
        meaning = cells[3].text
        flashcard['back'] .append(f'{meaning} [{origin}]')

    df = pd.DataFrame(flashcard)
    df = df[['front', 'back']]
    df.to_csv('katakana_flashcards.csv', sep='\t', index=False, header=False)
