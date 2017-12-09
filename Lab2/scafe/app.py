from urlib.request import urlopen
from bs4 import BeautifulSoup
import codecs
import pyexcel

raw_data = urlopen('http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn').read().decode('utf8')

file = codes.open
