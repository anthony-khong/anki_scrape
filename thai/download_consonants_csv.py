import pandas as pd

from anki_scrape import scrape

if __name__ == '__main__':
    url = 'https://en.wikipedia.org/wiki/Thai_alphabet'
    soup = scrape.get_soup(url)

    is_valid_row = lambda cells: len(cells) == 9 and cells[-2]
    filtered_rows = scrape.filter_rows(soup, is_valid_row)
    filtered_rows = list(filtered_rows)[:44]

    flashcard = {'front': [], 'back': []}
    for cells in filtered_rows:
        thai_word = cells[1].text
        flashcard['front'].append(thai_word)
        meaning = cells[3].text
        flashcard['back'] .append(meaning)

    df = pd.DataFrame(flashcard)
    df = df[['front', 'back']]
    df.to_csv('consonants_flashcards.csv', sep='\t', index=False, header=False)
