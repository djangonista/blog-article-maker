import config
import html_read
import requests
from bs4 import BeautifulSoup
from pylatex import Document, Package

picture_iterator = 0
if __name__ == '__main__':
    for key in config.POSTS_DICT:
        url = config.POSTS_DICT[key][0]
        response = requests.get(config.POSTS_DICT[key][0])
        soup = BeautifulSoup(response.text, 'lxml')
        post_title = soup.find(config.POSTS_DICT[key][1],attrs={'class': config.POSTS_DICT[key][2]})
        post_content = soup.find(config.POSTS_DICT[key][3], attrs={'class': config.POSTS_DICT[key][4]})
        document = Document()
        # usuniecie wciec w dokumencie
        document.preamble.append(Package('parskip'))


        elements = post_content.findAll()
        for element in elements:
            if element.name == 'p':
                html_read.p_tag_blockquote(element, document)
            elif element.name == 'img':
                html_read.img_tag(element,document,picture_iterator,config.IMG_WIDTH)
                picture_iterator += 1
            elif element.name == 'ul':
                html_read.ul_tag(element,document)
            elif element.name == 'ol':
                html_read.ol_tag(element,document)

        document.generate_pdf(post_title.get_text().rstrip())



