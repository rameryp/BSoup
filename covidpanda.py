###################################################################
## Read COVID 19 Stats from https://www.worldometers.info/coronavirus/
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

# Retrieve latest proxies
myRequest = Request('https://www.worldometers.info/coronavirus/')
myRequest.add_header('User-Agent', ua.random)
myRequest_doc = urlopen(myRequest).read().decode('utf8')

soup = BeautifulSoup(myRequest_doc, 'html.parser')
full_content = soup.find(id='main_table_countries_today')
table_rows = full_content.find_all('tr')

country_data =[]

def myInt(a):
    if a:
          return a
    else:
          return 0

for tr in table_rows[9:-9]:  #skip regions row at the beginning and total rows at the end
  # get all rows
  td = tr.find_all('td')
  # remove trailing spaces
  row = [i.text.strip() for i in td]
  #clean up rows
  row[1:11] = [x.replace(',', '') for x in row[1:11]]
  row[1:11] = [x.replace('+', '') for x in row[1:11]]
  # convert string to int while managing empty value 
  row[1:11] = map(myInt,row[1:11])
  # add cleaned row
  country_data.append(row)
  
#print(country_data)


####################################################################

def main():  
  clearScreen()
  Countries  = []
  TotalCases = []	
  NewCases	 = []	
  TotalDeaths= []	
  NewDeaths	 = []	

  for row in country_data:
    #if row: #not empty
    #print (row[0]+' - '+str(row[1])+' - '+str(row[2])+' - '+str(row[3])+' - '+str(row[4])+' - '+str(row[5])+' - '+str(row[6]))
    Countries.append(row[0])
    TotalCases.append(row[1])
    NewCases.append(row[2])
    TotalDeaths.append(row[3])
    NewDeaths.append(row[4])

  print(TotalCases)
  print(Countries)

if __name__ == "__main__":
      main()



#TotalRecovered  = []	
#ActiveCases	 = []	
#SeriousCritical	 = []	
#TotCases1M  = []	
#Deaths1Mpop = []	
#TotalTests	 = []	
#Tests1M = []	