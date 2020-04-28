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
myRequest = Request('https://www.worldometers.info/coronavirus/')
myRequest.add_header('User-Agent', ua.random)
myRequest_doc = urlopen(myRequest).read().decode('utf8')

soup = BeautifulSoup(myRequest_doc, 'html.parser')
full_content = soup.find(id='main_table_countries_today')
table_rows = full_content.find_all('tr')

country_data =[]

for tr in table_rows:
  td = tr.find_all('td')
  row = [i.text.strip() for i in td]
  country_data.append(row)
  


####################################################################

def main():  
  clearScreen()
  print ('COVID Dump')
  print ('####################################'+'\n')

  print (table_rows)

if __name__ == "__main__":
      main()

