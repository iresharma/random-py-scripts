import requests
from bs4 import BeautifulSoup

lists = []

def downloadImage(href: str):
    URL = f'https://github.com/{href}'
    response = requests.get(URL)
    imagePage = BeautifulSoup(response.content, 'html.parser')
    fileName = imagePage.find('strong', attrs={'class': "final-path"}).text
    lists.append(fileName.split('.')[0].split('@')[0])
    # filePath = imagePage.find('img', attrs={'class': None, 'id': None}).attrs['src']
    # print(filePath)
    # imageReq = requests.get(f'https://github.com/{filePath}')
    # # print(imageReq.content)
    # with open(f'assets/{fileName}', 'wb') as img:
    #     img.write(imageReq.content)

URL = "https://github.com/twostraws/HackingWithSwift/tree/main/SwiftUI/project2-files"

response = requests.get(URL)
# pprint(response.content)

with open('github.html', 'wb') as html:
    html.write(response.content)

githubPage = BeautifulSoup(response.content, 'html.parser')

for link in githubPage.find_all('a', attrs={'class': "js-navigation-open Link--primary"}):
    downloadImage(link.attrs['href'])

print(list(set(lists)))