import config
from pylatex import Command, NoEscape, Itemize, Enumerate, Figure
import wget

def p_tag(element, document):
    for string in element.strings:
        if string.parent.name == 'strong':
            document.append(Command('textbf',string))
            document.append(NoEscape(r'\space'))
        else:
            document.append(string)
        if string.next_element.name == 'br':
            document.append(Command('newline'))
    document.append(Command('par'))


def p_tag_blockquote(element, document):
    if element.parent.name == 'blockquote':
        document.append(NoEscape(r'\begin{quote}'))
        p_tag(element,document)
        document.append(NoEscape(r'\end{quote}'))
    else:
        p_tag(element,document)

def ul_tag(element,document):
    with document.create(Itemize()) as itemize:
        for item in element.findAll():
            if item.name == 'li':
                itemize.add_item(item.get_text())
        itemize.append(Command("ldots"))

def ol_tag(element, document):
    with document.create(Enumerate()) as enum:
        for item in element.findAll():
            if item.name == 'li':
                enum.add_item(item.get_text())

def img_tag(element,document,picture_iterator,pic_width):
    with document.create(Figure(position='h!')) as picture:
        if element.parent.name == 'a' and  element.parent['href'].endswith('.jpg'):
            file_pic = wget.download(element.parent['href'],str(picture_iterator) +'.jpg')
            picture.add_image(file_pic, width=pic_width)
        elif 'data-src' in element.attrs:
            file_pic = wget.download(element['data-src'], str(picture_iterator) + '.jpg')
            picture.add_image(file_pic, width=pic_width)
        else:
            file_pic = wget.download(element['src'], str(picture_iterator) + '.jpg')
            picture.add_image(file_pic, width=pic_width)