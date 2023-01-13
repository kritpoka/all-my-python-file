import requests
from bs4 import BeautifulSoup

url_youtube = "https://www.youtube.com"
url_borntodev = "https://www.borntodev.com"

web_youtube = requests.get(url_youtube)
web_borntodev = requests.get(url_borntodev)

soup_youtube = BeautifulSoup(web_youtube.text, 'html.parser')
find_youtube = soup_youtube.find_all()

soup_borntodev = BeautifulSoup(web_borntodev.text, 'html.parser')
find_borntodev = soup_borntodev.find_all()

for i in find_youtube:
    print(i)

for i in find_borntodev:
    print(i)
