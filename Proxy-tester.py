import requests
from colorama import Fore

input_proxy = input('Enter your proxy file(No need add .txt): ')
input_proxy = input_proxy + '.txt'

with open(input_proxy, 'r') as file:
    proxies = file.readlines()

for proxy in proxies:
    proxy = proxy.strip()
    proxy = {'http': 'http://' + proxy}


    response = requests.get(url='https://google.com', proxies=proxy)
    if response.status_code == 200:
        print(Fore.GREEN + 'Proxy is work: ' + proxy['http'])
    else:
       print(Fore.RED + 'This proxy not work: ' + proxy['http'] + '    Error code: ' + str(response.status_code))
