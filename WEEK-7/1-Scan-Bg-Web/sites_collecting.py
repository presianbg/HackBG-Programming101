import requests
from bs4 import BeautifulSoup


def main():
    r = requests.get("http://register.start.bg/")
    soup = BeautifulSoup(r.text)

    for link in soup.find_all('a'):
        ff = requests.head("http://register.start.bg/{}".format(link.get('href')))
        try:
            print(ff.status_code)
        except:
            KeyError

if __name__ == '__main__':
    main()
