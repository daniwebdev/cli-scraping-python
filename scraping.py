from bs4 import BeautifulSoup
import requests as req
import re


link = input('URL: ') or 'https://detik.com'
tag  = input('Tag (div,span,etc): ')
selector  = input('Selector (Class(.class),Id(#id)): ')

try:
    html    = req.get(link)
    parser  = BeautifulSoup(html.text, "html.parser")

    if selector.find('.') == 0:
        params = {"class": re.sub(r"\.(\w+)", r"\1", selector) }
    elif selector.find('#') == 0:
        params = {"id": re.sub(r"\#(\w+)", r"\1", selector) }

    get_parse = parser.findAll(tag, params)

    for index, data in enumerate(get_parse):
        print(data.text.strip())

except req.exceptions.RequestException as error:
    print(error)