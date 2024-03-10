import requests

input_proxy = input('Enter your proxy file(No need add .txt): ')
input_proxy = input_proxy + '.txt'

with open(input_proxy,'r') as file:
    proxys = file.readlines()
    
    
for proxy in proxys:
    proxy = proxy.strip()
    proxy = {'http': 'http://' + proxy}

    r = requests.get(url='https://chamranvoc.ir', proxies=proxy)
    with open('ashhsd.html','w',encoding='utf8') as file:
        file.write(r.text)
