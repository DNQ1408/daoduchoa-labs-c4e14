from youtube_dl import YoutubeDL

# #Download a single youtube video
# dl = YoutubeDL()
# dl.download(['https://www.youtube.com/watch?v=WHK5p7JL7g4'])

# # Download multiple youtube videos
# dl = YoutubeDL()
# # Put list of song urls in download function to download them, one by one
# dl.download(['https://www.youtube.com/watch?v=wNVIn-QS4DE', 'https://www.youtube.com/watch?v=JZjRrg2rpic'])

# #  Download audio
# options = {
#     'format': 'bestaudio/audio' # Tell the downloader to download only the best quality of audio
# }
# dl = YoutubeDL(options)
# dl.download(['https://www.youtube.com/watch?v=JZjRrg2rpic'])

# # Search and then download the first video
# options = {
#     'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
#     'max_downloads': 1 # Tell downloader to download only the first entry (video)
# }
# dl = YoutubeDL(options)
# dl.download(['con điên TAMKA PKL'])


# # Search and then download the first audio
# options = {
#     'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
#     'max_downloads': 1, # Tell downloader to download only the first entry (audio)
#     'format': 'bestaudio/audio'
# }
# dl = YoutubeDL(options)
# dl.download(['Nhớ mưa sài gòn lam trường'])
