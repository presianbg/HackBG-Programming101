import requests
from bs4 import BeautifulSoup
import re


def main():
    is_link = r'^(http|https)://'
    r = requests.get("http://katalog.start.bg/%D0%9C%D1%83%D0%B7%D0%B8%D0%BA%D0%B0/#c165")
    soup = BeautifulSoup(r.text)
    is_startbg = 'start.bg'
    sub_catalog = set()

    for link in soup.find_all('a'):
        if re.match(is_link, str(link.get('href'))):
            if is_startbg not in link.get('href'):
                print('/'.join(link.get('href').split('/')[:3]))
            else:
                sub_catalog.add(link.get('href'))

    print (sub_catalog)


if __name__ == '__main__':
    main()
