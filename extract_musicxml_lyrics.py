"""Pull the lyrics out of a MusicXML document."""

from bs4 import BeautifulSoup


def main():
    """Put the docstring here."""
    musicxml_filepath = input('Uncompressed MusicXML filepath: ')

    with open(musicxml_filepath, 'r') as m:
        music = m.read()

    soup = BeautifulSoup(music, 'xml')

    words = []
    last_syl = ''

    for lyric in soup.find_all('lyric'):
        syl = lyric.find('text').string if lyric.find('text') else ''
        syl_type = lyric.find('syllabic').string \
            if lyric.find('syllabic') else ''

        # https://www.musicxml.com/tutorial/the-midi-compatible-part/lyrics/
        if syl_type == 'single':
            word = syl
        elif syl_type == 'begin':
            last_syl = syl
            continue
        elif syl_type == 'middle':
            last_syl = last_syl + syl
            continue
        elif syl_type == 'end':
            word = last_syl + syl
        else:
            continue
        words.append(word)

    full_text = ' '.join(words)
    print(full_text)


if __name__ == '__main__':
    main()
