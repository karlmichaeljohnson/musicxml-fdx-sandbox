"""Put the docstring here."""

from bs4 import BeautifulSoup


def main():
    """Put the docstring here."""
    fd_sample = 'sample.fdx'
    with open(fd_sample, 'r') as f:
        fd_text = f.read()

    soup = BeautifulSoup(fd_text, 'xml')

    words = []
    for text_tag in soup.find_all('Text'):
        if text_tag.string and text_tag.string != '':
            word = text_tag.string
            words.append(word)
        else:
            continue

        print('Successful.')


if __name__ == '__main__':
    main()
