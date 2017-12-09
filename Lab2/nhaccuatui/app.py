from urllib.request import urlopen
from bs4 import BeautifulSoup
import codecs
html_content = urlopen('https://www.nhaccuatui.com/bai-hat/top-20.au-my.html').read().decode('utf8')
import pyexcel
# file = codecs.open('nct.html', 'w', 'utf8') # w= write, b= binary(raw)
# file.write(raw_data)
# file.close()

soup = BeautifulSoup(html_content, 'html.parser')
ul = soup.find('ul', 'list_show_chart')
li_list = ul.find_all('li')

new_list = []

for li in li_list:
    h3 = li.h3
    title = h3.a
    h4 = li.h4

    artist_list = h4.find_all('a')

    single = ''

    for artist in artist_list:
        single += artist.string + ','

    news = {
        'title': title.string,
        'artist': single
    }

    new_list.append(news)

pyexcel.save_as(records = new_list, dest_file_name='nhaccuatui.xlsx')
