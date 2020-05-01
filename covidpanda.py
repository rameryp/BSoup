########################################################################
## Read COVID 19 Stats from https://www.worldometers.info/coronavirus/
#######################################################################
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import pandas as pd

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

def mk_int(s):
    s = s.strip()
    if s =='N/A':
          s=0 
    return float(s) if s else 0

def cleanArray(dirtyArray):
      cleanedArray = []
      cleanedArray = [x.replace(',', '') for x in dirtyArray]
      cleanedArray = [x.replace('+', '') for x in cleanedArray]
      return cleanedArray
    
def main():      
  #for tr in table_rows[9:-9]:  #skip regions row at the beginning and total rows at the end
  for tr in table_rows[9:29]:  #skip regions row at the beginning and total rows at the end
    # get all rows
    td = tr.find_all('td')
    # remove trailing spaces
    row = [i.text.strip() for i in td]
    row[1:11] = cleanArray(row[1:11])
    row[1:11] = map(mk_int,row[1:11])
    # add cleaned row
    country_data.append(row)


  Countries  = []
  TotalCases = []	
  NewCases	 = []	
  TotalDeaths= []	
  NewDeaths	 = []	
  TotalRecovered  = []	
  ActiveCases	 = []	

  for row in country_data:
    Countries.append(row[0])
    TotalCases.append(row[1])
    NewCases.append(row[2])
    TotalDeaths.append(row[3])
    NewDeaths.append(row[4])
    TotalRecovered.append(row[5])
    ActiveCases.append(row[6])

  data_dict = {
    #'Countries':Countries,
    #'TotalCases':TotalCases,
    #'NewCases':NewCases,
    'TotalDeaths':TotalDeaths,
    #'NewDeaths':NewDeaths,
    'TotalRecovered':TotalRecovered,
    #'ActiveCases':ActiveCases 
  }

  #columns = ['Countries','TotalCases','NewCases','TotalDeaths','NewDeaths','ActiveCases' ]
  columns = ['TotalDeaths','TotalRecovered' ]
  df = pd.DataFrame(data_dict, columns=columns,index=Countries)

    
  print(df)

if __name__ == "__main__":
      main()




#SeriousCritical	 = []	
#TotCases1M  = []	
#Deaths1Mpop = []	
#TotalTests	 = []	
#Tests1M = []	