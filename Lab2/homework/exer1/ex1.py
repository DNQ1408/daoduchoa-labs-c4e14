# Part 1
from urllib.request import urlopen
from bs4 import BeautifulSoup
from youtube_dl import YoutubeDL
import pyexcel

html_content = urlopen('https://www.apple.com/itunes/charts/songs/').read().decode('utf8')

# ROI
soup = BeautifulSoup(html_content, 'html.parser')
section = soup.find('section', 'section chart-grid')
ul = section.div.ul
li_list = ul.find_all('li')

# # Exact
song_list = []
for li in li_list:
    title = li.h3.a

    artist_list = li.h4.find_all('a')
    artists = ''
    for artist in artist_list:
        artists += artist.string + ' '

    song = {
        'Title' : title.string,
        'Artist' : artists
    }

    song_list.append(song)
pyexcel.save_as(records= song_list, dest_file_name= 'Itunes_top_songs.xlsx')


# Part 2

from youtube_dl import YoutubeDL

options = {
    'default_search' : 'ytsearch',
    'max_download' : len(song_list)
}

dl = YoutubeDL(options)

for song in song_list:
    dl.download([song['Title'] +" "+ song['Artist']])
