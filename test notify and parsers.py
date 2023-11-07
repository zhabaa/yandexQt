from subfunc.Notify import ShowNotify
from subfunc.Parsers import Parse

from pprint import pprint

parser = Parse()
ntf = ShowNotify()


for kind in ['news', 'rate', 'weather']:
    if kind == 'weather':
        data = parser.parse_weather('Сыктывкар')
    if kind == 'rate':
        data = parser.parse_rate()
    if kind == 'news':
        data = parser.parse_news()
    pprint(data)

ntf.show_notify(kind=kind, data=data)
