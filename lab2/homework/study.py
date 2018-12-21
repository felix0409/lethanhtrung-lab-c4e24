from youtube_dl import YoutubeDL

#Videos Download
dl = YoutubeDL()
dl.download(["https://www.youtube.com/watch?v=xhAWFVgGVAk", "https://www.youtube.com/watch?v=mTQA9wjcjsE"])

#Audio Download
options = {
    'format': 'bestaudio/audio' # Tell the downloader to download only the best quality of audio
}
dl = YoutubeDL(options)
dl.download(['https://www.youtube.com/watch?v=mTQA9wjcjsE'])

# Sample 4: Search and then download the first video
options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1 # Tell downloader to download only the first entry (video)
}
dl = YoutubeDL(options)
dl.download(['Thương em là điều không thể ngờ sing my song'])


# Sample 5: Search and then download the first audio
options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1, # Tell downloader to download only the first entry (audio)
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['Nhớ mưa sài gòn lam trường'])
