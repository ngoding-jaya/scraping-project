import requests
from bs4 import BeautifulSoup

html_doc = requests.get('https://www.detik.com/terpopuler/sepakbola?', params={'_ga': '2.247927687.1076782796.1653400058-1590184724.1649902310'})
soup = BeautifulSoup(html_doc.text, 'html.parser')
populer_area = soup.find(attrs={'class': 'grid-row list-content'})
titles = populer_area.findAll(attrs={'class': 'media__title'})
images = populer_area.findAll(attrs={'class': 'media__image'})

for image in images:
    print(image.find('a').find('img')['title'])
