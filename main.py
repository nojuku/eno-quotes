from lxml import html
import requests

page = requests.get('http://stoney.sb.org/eno/oblique.html')
tree = html.fromstring(page.content)

quote = tree.xpath('/html/body/center/h3/text()')

print(quote)