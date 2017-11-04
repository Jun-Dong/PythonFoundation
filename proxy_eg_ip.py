import urllib.request
import random

url = 'http://www.whatismyip.com.tw/'

iplist = ['123.152.76.92:811', '219.133.160.219:8118','112.226.232.186:8118','61.135.217.7:80']

proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})

opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')]


urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

print(html)
