from requests import get
from bs4 import BeautifulSoup

data = get('https://github.com/twostraws/HackingWithSwift/tree/main/SwiftUI/project8-files/Images')
soup = BeautifulSoup(data.content, 'html.parser')

links = []

refs = soup.find_all("a", {'class': 'js-navigation-open Link--primary'})
for i in refs:
    links.append(f'https://github.com{i["href"]}')

soups = []
for i in links:
    print(i.split('/')[-1])
    data = get(i)
    soup = BeautifulSoup(data.content, 'html.parser')
    img = soup.find("div", {'class': 'blob-wrapper'}).div.span.img['src']
    imgRes = get(f'https://github.com{img}')
    print(f'https://github.com{img}')
    with open(f'images/{i.split("/")[-1].replace("%40", "@")}', 'wb') as imgFile:
        imgFile.write(imgRes.content)
