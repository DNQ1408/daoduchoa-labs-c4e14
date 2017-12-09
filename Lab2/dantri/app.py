from urllib.request import urlopen
from bs4 import BeautifulSoup # Camel Case
import pyexcel
# 1. Download dantri hompage
webpage = urlopen('http://dantri.com') # Open connection
data = webpage.read()
html_content = data.decode('utf8') # Type: string
# print(html_content)

# 2. Analyze ROI (Regional of Interest)
# 2.1 Creat BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
ul = soup.find('ul', 'ul1 ulnew') # Find one
li_list = ul.find_all('li')
# for li in li_list:
#     print(li.prettify())
#     print('*'*20)




#3. Extract data from ROI

new_list = []
for li in li_list:
    h4 = li.h4 # Find h4
    a = h4.a
    news = {
    'tilte': a.string,
    'link': 'http://dantri.com' + a['href']
    }
    # print(news)
    new_list.append(news)
    # print(new_list)

pyexcel.save_as(records= new_list, dest_file_name= 'dantri.xlsx')


# Scrape cho html + ajax -> dùng tool selenium
