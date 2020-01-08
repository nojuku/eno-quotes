import os
import requests
from lxml import html
from flask import Flask

def scrape():

	page = requests.get('http://stoney.sb.org/eno/oblique.html')
	tree = html.fromstring(page.content)
	quote = tree.xpath('/html/body/center/h3/text()')

	return str(quote[0])

app = Flask(__name__)

@app.route('/')
def hello():
    return scrape()

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

