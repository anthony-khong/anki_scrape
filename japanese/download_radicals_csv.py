import pandas as pd

from anki_scrape import scrape

if __name__ == '__main__':
    url = 'https://kanjialive.com/214-traditional-kanji-radicals/'
    soup = scrape.get_soup(url)

    is_valid_row = lambda cells: len(cells) == 7
    filtered_rows = scrape.filter_rows(soup, is_valid_row)

    flashcard = {'front': [], 'back': []}
    for cells in filtered_rows:
        radical = cells[1].text
        flashcard['front'].append(radical)
        meaning = cells[3].text
        flashcard['back'] .append(meaning)

    df = pd.DataFrame(flashcard)
    df = df[['front', 'back']]
    df.to_csv('radicals_flashcards.csv', sep='\t', index=False, header=False)
