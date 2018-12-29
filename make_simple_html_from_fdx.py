"""Put docstring here."""

from bs4 import BeautifulSoup


def main():
    """Put the docstring here."""
    fd_sample = 'sample2.fdx'
    with open(fd_sample, 'r') as f:
        fd_text = f.read()

    soup = BeautifulSoup(fd_text, 'xml')

    paras = soup.find_all('Paragraph')

    html = '<html><head></head><body><div style="margin-left:250px; margin-right:250px;">'

    for para in paras:
        # Some paragraphs have more than one <Text></Text> tag in them.
        if para.find('Text').string:
            para_text = para.find('Text').string
            if para.get('Type') == 'Character':
                para_string = ('<p style="margin-left:300px; font-weight:bold;">'
                               '{}</p>\n'.format(para_text.upper()))
            elif para.get('Type') == 'Action':
                if para_text.lower().startswith('act') or para_text.lower().startswith('teaser'):
                    para_string = '<hr><p style="margin-left:300px;">{}</p>\n'.format(para_text.upper())
                else:
                    para_string = '<p style="margin-left:100px; font-style:italic;">{}</p>\n'.format(para_text)
            elif para.get('Type') == 'Dialogue':
                para_text = ''
                for text_block in para.find_all('Text'):
                    if text_block.string:
                        para_text += text_block.string
                    para_string = '<p>{}</p>\n'.format(para_text)
            else:
                para_string = '<p>{}</p>'.format(para_text)
        else:
            para_string = ''

        html += para_string

    html += '</div></body></html>'

    with open('test.html', 'w') as f:
        f.write(html)


if __name__ == '__main__':
    main()
