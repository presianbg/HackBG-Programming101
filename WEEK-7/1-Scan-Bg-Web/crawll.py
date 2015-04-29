import requests
from bs4 import BeautifulSoup
import re


def main():
    is_link = re.compile(r'^(http|https)://')
    is_catalog_link = r'^(http|https)://katalog'
    is_startbg = ('start.bg', 'start.bg/')
    is_redirect_link = r'^link.php[?]id='
    source = requests.get("http://www.start.bg/")
    soup = BeautifulSoup(source.text)
    ext_sites = set()
    catalogs = set()
    sub_catalogs = set("http://register.start.bg/")

    for link in soup.find_all('a'):
        c_url = str(link.get('href'))
        if re.match(is_catalog_link, c_url):
            catalogs.add(c_url)
        elif is_link.match(c_url) and c_url.endswith(is_startbg):
            sub_catalogs.add(c_url)

    for catalog in catalogs:
        print (catalog)

if __name__ == '__main__':
    main()
