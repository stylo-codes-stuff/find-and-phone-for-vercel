import requests
from bs4 import BeautifulSoup
baseURL = "http://165.227.37.175/callers/browse/"
new_list = []
def sphinxFetch(number):
    new_list.clear()
    print(number)
    req = requests.get(url=baseURL + number)
    print(baseURL+number)
    soup = BeautifulSoup(req.text, features="html.parser")
    res = [p.text.strip() for p in soup.select('p')]  # https://stackoverflow.com/questions/40716272/how-to-extract-h1-tag-text-with-beautifulsoup
    for x in res:
        x = x.replace("\r","")
        x = x.replace("\t","")
        x = x.replace("  ","")
        new_list.append(x)
    print(new_list)
    return new_list
