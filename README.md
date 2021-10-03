# HideMe [![Python Badge](https://img.shields.io/badge/-Python-00000??style=flat-square&logo=python&logoColor=FFD43B&color=informational)](https://www.python.org/downloads/) [![Build Status](https://app.travis-ci.com/eckarthik/HideMe.svg?branch=master)](https://app.travis-ci.com/eckarthik/HideMe) [![Downloads](https://pepy.tech/badge/hideme)](https://pepy.tech/project/hideme) [![Downloads](https://pepy.tech/badge/hideme/week)](https://pepy.tech/project/hideme/week)

HideMe is a python package for gathering usable proxies from free proxy webites
can be installed via pip as follows.
Believe me It's fast

```
pip install hideme
```

## Documentation

Format of proxies returned by **HideMe** is as shown below
```python
[
   {
      "ip_address":"XX.XXX.XXX.XX",
      "port":"XXXX",
      "country_code":"DE",
      "country":"Germany",
      "anonymity":"anonymous",
      "google_support":False,
      "https":False
   }
]
```
You can get the proxies by creating a **ProxiesList** object and then calling get method on that

```python
from hideme.proxy_collector import ProxiesList
proxy_list = ProxiesList()
proxy = proxy_list.get()
```

Output:

```python
[
   {
      "ip_address":"88.198.50.103",
      "port":"8080",
      "country_code":"DE",
      "country":"Germany",
      "anonymity":"anonymous",
      "google_support":False,
      "https":False
   }
]
```

You can restrict the required number of proxies returned by passing count param to the get method.

```python
from hideme.proxy_collector import ProxiesList
proxies_list = ProxiesList()
proxies = proxies_list.get(count=2)
```

Output:

```python
[
   {
      "ip_address":"88.198.50.103",
      "port":"8080",
      "country_code":"DE",
      "country":"Germany",
      "anonymity":"anonymous",
      "google_support":False,
      "https":False
   },
   {
      "ip_address":"187.45.123.137",
      "port":"36559",
      "country_code":"BR",
      "country":"Brazil",
      "anonymity":"elite proxy",
      "google_support":False,
      "https":True
   }
]
```



You can also filter out the returned proxies by passing the filter params to the **ProxiesList** class. Example usages:-

This will return only those proxies which are in Country - **Spain**

```python
from hideme.proxy_collector import ProxiesList
proxies_list = ProxiesList(country='Spain')
proxies = proxies_list.get()
```

Output:
```python
[
   {
      "ip_address":"185.44.232.30",
      "port":"53281",
      "country_code":"ES",
      "country":"Spain",
      "anonymity":"elite proxy",
      "google_support":False,
      "https":False
   },
   {
      "ip_address":"82.223.3.52",
      "port":"8118",
      "country_code":"ES",
      "country":"Spain",
      "anonymity":"elite proxy",
      "google_support":False,
      "https":False
   }
]
```

This will return only those proxies which are HTTPS supported

```python
from hideme.proxy_collector import ProxiesList
proxies_list = ProxiesList(https=True)
proxies = proxies_list.get()
```

Output
```python
[
   {
      "ip_address":"201.217.4.101",
      "port":"53281",
      "country_code":"PY",
      "country":"Paraguay",
      "anonymity":"elite proxy",
      "google_support":False,
      "https":True
   },
   {
      "ip_address":"13.233.160.59",
      "port":"80",
      "country_code":"IN",
      "country":"India",
      "anonymity":"elite proxy",
      "google_support":False,
      "https":True
   }
]
```

You can also combine multiple filter params like below
```python
from hideme.proxy_collector import ProxiesList
proxies_list = ProxiesList(country='India',https=True,port='80',google_support=False)
proxies = proxies_list.get()
```

Output

```python
[
   {
      "ip_address":"13.233.160.59",
      "port":"80",
      "country_code":"IN",
      "country":"India",
      "anonymity":"elite proxy",
      "google_support":False,
      "https":True
   }
]
```


