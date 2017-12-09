from urllib.request import urlopen
from bs4 import BeautifulSoup
import codecs

# HTML file:
html_content = urlopen('http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn').read().decode('utf8')
# file = codecs.open('scafe.html','w','utf8')
# file.write(html_content)
# file.close()

#ROI
soup = BeautifulSoup(html_content,'html.parser')
table = soup.find('table',{'id':'tableContent'})
tr_list = table.find_all('tr')
bao_cao = {}
ban_bao_cao = []
list1 = ['Quý 4-2016', 'Quý 1-2017', 'Quý 2-2017', 'Quý 3-2017']

for tr in tr_list:
    solieu = tr.find_all('td',{'style':"width:15%;padding:4px;color:#014377;font-weight:bold;"})
    tieude = tr.find('td',{'style':"width:32%;color:#014377;font-weight:bold;"})
    if tieude != None:
        list2 = []
        for item in solieu:
            so_lieu = item.string
            list2.append(so_lieu)
        bao_cao = dict(zip(list1,list2))
        bao_cao['Title'] = tieude.string

        ban_bao_cao.append(bao_cao)
    solieu_ = tr.find_all('td',{'style':"width:15%;padding:4px;color:#014377;"})
    tieude_ = tr.find('td',{'style':"width:32%;color:#014377;"})
    if tieude_ != None:
        list2 = []
        for item in solieu_:
            so_lieu = item.string
            list2.append(so_lieu)
        bao_cao = dict(zip(list1,list2))
        bao_cao['Title'] = tieude_.string

        ban_bao_cao.append(bao_cao)

import pyexcel
pyexcel.save_as(records= ban_bao_cao, dest_file_name= 'ban_bao_cao.xlsx')
