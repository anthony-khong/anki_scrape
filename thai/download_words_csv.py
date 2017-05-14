import pandas as pd

from anki_scrape import scrape

if __name__ == '__main__':
    url = 'http://1000mostcommonwords.com/1000-most-common-thai-words/'
    soup = scrape.get_soup(url)

    is_valid_row = lambda cells: len(cells) == 3
    filtered_rows = scrape.filter_rows(soup, is_valid_row)
    next(filtered_rows) # Need to throw away the header

    flashcard = {'front': [], 'back': []}
    for cells in filtered_rows:
        thai_word = cells[1].text
        flashcard['front'].append(thai_word)
        meaning = cells[2].text
        flashcard['back'] .append(meaning)

    df = pd.DataFrame(flashcard)
    df = df[['front', 'back']]
    df.to_csv('words_flashcards.csv', sep='\t', index=False, header=False)
