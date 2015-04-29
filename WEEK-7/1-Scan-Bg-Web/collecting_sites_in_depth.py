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
        s_url = str(link.get('href'))
        if re.match(is_catalog_link, s_url):
            catalogs.add(s_url)
        elif is_link.match(s_url) and s_url.endswith(is_startbg):
            sub_catalogs.add(s_url)
        elif is_link.match(s_url):
            ext_sites.add('/'.join(s_url.split('/')[:3]))

    for s_catalog in catalogs:
        sub_source = requests.get(s_catalog)
        soup_2 = BeautifulSoup(sub_source.text)
        for link in soup_2.find_all('a'):
            s2_url = str(link.get('href'))
            if is_link.match(s2_url) and s2_url.endswith(is_startbg):
                sub_catalogs.add(s2_url)
            elif is_link.match(s2_url):
                ext_sites.add('/'.join(s2_url.split('/')[:3]))

    for catlog in sub_catalogs:
        if is_link.match(catlog):
            site = requests.get(catlog)
            soup_3 = BeautifulSoup(site.text)
            for link in soup_3.find_all('a'):
                s3_url = str(link.get('href'))
                if re.match(is_redirect_link, s3_url):
                    redirect_url = catlog + s3_url
                    try:
                        ffl = requests.head(redirect_url, timeout=1.5)
                        site_url = (ffl.headers['location'])
                        if is_link.match(site_url):
                            norm_url = ('/'.join(site_url.split('/')[:3]))
                            print (norm_url)
                            ext_sites.add(norm_url)
                    except:
                        pass

    print (len(ext_sites))
    print (len(catalogs))
    print (len(sub_catalogs))

if __name__ == '__main__':
    main()
