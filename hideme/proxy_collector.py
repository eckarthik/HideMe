from urllib.request import urlopen,Request
import re,random,os

class ProxiesList:
    """Returns the proxies satisfying the given criteria"""

    def __init__(self,**kwargs):
        self.filter_criteria = kwargs
        self.user_agents = open(os.path.join(os.path.dirname(__file__), "user_agents.txt"),"r").read().split("\n")
        random.shuffle(self.user_agents)
        self.user_agent = self.user_agents[0]

    def format(self,proxy):
        """Take the proxy details tuple and make a dictionary out of it"""

        return {
            "ip_address":proxy[0],
            "port":proxy[1],
            "country_code":proxy[2],
            "country":proxy[3],
            "anonymity":proxy[4],
            "google_support":True if proxy[5] == 'yes' else False,
            "https":True if proxy[6] == 'yes' else False
        }

    def get_proxy_page(self):
        headers = {
            'User-Agent': self.user_agent,
            'Accept':
                'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Connection': 'keep-alive',
            'Content-Encoding': 'gzip',
            'Content-Type': 'text/html; charset=utf-8',
        }
        request = Request("https://free-proxy-list.net/",headers=headers)
        proxy_page_response = urlopen(request).read().decode()
        proxies = re.findall(r"<td>([0-9\.]*)</td><td>([0-9]*)</td><td>([A-Z]{2})</td><td class='hm'>([a-zA-Z]*)</td>"
                             r"<td>([a-zA-Z ]*)</td><td class='hm'>([a-z]*)</td><td class='hx'>([a-zA-Z]*)</td>",
                             proxy_page_response)
        return [self.format(proxy) for proxy in proxies]

    def filter_proxies(self):
        """Filters the proxies based on the given params and returns the proxy list"""

        proxies_list = self.get_proxy_page()
        for k,v in self.filter_criteria.items():
            proxies_list = list(filter(lambda x:x[k] == v,proxies_list))
        return list(proxies_list)

    def get(self,count=100):
        """Returns the requested number of proxies. Returns 100 proxies by default"""

        return self.filter_proxies()[:count]