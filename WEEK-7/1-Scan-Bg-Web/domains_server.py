import requests
import pickle
from histogram import Histogram


def main():
    domains = set()
    with open('ext_sites.bin', 'rb') as domainf:
            domains = pickle.load(domainf)

    srv_distribution = Histogram()

    our_headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36"
    }

    for domain in domains:
        try:
            rq_head = requests.head(domain, timeout=0.5, headers=our_headers)
            srv = (rq_head.headers['Server'])
            general_srv = srv.split('/')[0]
            srv_distribution.add(general_srv)
        except:
            pass

    srv_histogram = srv_distribution.get_dict()

    with open('server_distribution.bin', 'wb') as srvf:
        pickle.dump(srv_histogram, srvf)


if __name__ == '__main__':
    main()
