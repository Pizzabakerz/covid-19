import bs4 as bs
import pandas as pd
from urllib.request import Request, urlopen

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

req = Request('https://www.promptcloud.com/coronavirus-tracker/"', headers={'User-Agent': 'Mozilla/5.0'})

print("--------- Fetched url --------------")

sauce = urlopen(req).read()
soup = bs.BeautifulSoup(sauce,'lxml')

print("--------- Processing Data --------------")

data = []
rows = soup.find_all('tr')
for row in range(1,len(rows)):
        cols = rows[row].find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append(cols)
print("--------- Exporting Data --------------")    
# print(data)
data = pd.DataFrame(data,columns = {'Country':'','TotalCases':float(),'NewCases':float(),'TotalDeaths':float(),'NewDeaths':float(),'TotalRecovered':float(),'ActiveCases':float(),'Serious Critical':float(),'Tot Cases per 1M pop':float()})
data.to_csv("covid19.csv",index=False)

print("--------- Processing Data --------------")
