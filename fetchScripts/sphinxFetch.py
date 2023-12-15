import requests
from bs4 import BeautifulSoup

baseURL = "http://165.227.37.175/callers/browse/214-218-3797"

req = requests.get(url=baseURL + "214-218-3797")
soup = BeautifulSoup(req.text, features="html.parser")
res = [p.text.strip() for p in soup.select('p')]  # https://stackoverflow.com/questions/40716272/how-to-extract-h1-tag-text-with-beautifulsoup
print(res)