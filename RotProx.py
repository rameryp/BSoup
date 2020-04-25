###################################################################
## ROTATING PROXIES
###################################################################
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random

def clearScreen():
  print(chr(27)+'[2j')
  print('\033c')
  print('\x1bc')

ua = UserAgent() # From here we generate a random user agent
proxies = [] # Will contain proxies [ip, port] 

# Retrieve latest proxies
proxies_req = Request('https://www.sslproxies.org/')
proxies_req.add_header('User-Agent', ua.random)
proxies_doc = urlopen(proxies_req).read().decode('utf8')

soup = BeautifulSoup(proxies_doc, 'html.parser')
proxies_table = soup.find(id='proxylisttable')

# Retrieve a random index proxy (we need the index to delete it if not working)
def getRandomProxyIndex():
  return random.randint(0, len(proxies) - 1)

# Save proxies in the array
def readInProxies():
  for row in proxies_table.tbody.find_all('tr'):
    proxies.append({
      'ip':   row.find_all('td')[0].string,
      'port': row.find_all('td')[1].string,
      'country': row.find_all('td')[3].string
    })
    a= row.find_all('td')[0].string
    print (a)

####################################################################

def main():  
  clearScreen()
  print ('Dumping proxy list')
  print ('####################################'+'\n')

  readInProxies()
  #print(len(proxies))
  randomIndex = getRandomProxyIndex()
  #print (proxy_index)
  print (proxies[randomIndex])

if __name__ == "__main__":
      main()

