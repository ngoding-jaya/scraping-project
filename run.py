import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('detik.html')


@app.route('/detik-bola')
def detik_bola():
    html_doc = requests.get('https://www.detik.com/terpopuler/sepakbola?',
                            params={'_ga': '2.247927687.1076782796.1653400058-1590184724.1649902310'})
    soup = BeautifulSoup(html_doc.text, 'html.parser')
    populer_area = soup.find(attrs={'class': 'grid-row list-content'})
    images = populer_area.findAll(attrs={'class': 'media__image'})
    print(images)
    return render_template('detik.html', images=images)


if __name__ == '__main__':
    app.run(debug=True)
