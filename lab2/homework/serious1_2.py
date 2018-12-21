from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel #as p
from collections import OrderedDict
from youtube_dl import YoutubeDL

#1. download trang
url = "https://www.apple.com/itunes/charts/songs"
#1.1 Open a connection to server
conn = urlopen(url)

#1.2 Read data
raw_data = conn.read()
#1.3 Decode data
page_content = raw_data.decode("utf8")

# print(page_content)

# f = open("dantri.html", "wb")
# f.write(raw_data)
# f.close()


#2. Extract ROI (Region of Interest)
soup = BeautifulSoup(page_content, "html.parser")
section = soup.find("section", "section chart-grid") #.find(ten the, nhan dang them) class thi k can them. #neu k phai la class thi phai them
#id="uli ulnew"
div = section.find("div", "section-content")
ul = div.find("ul")
# print(ul) #.prettify: lam dep
#la 1 soup thi moi' prettify duoc 
li_list = ul.find_all("li")
print(li_list)

#3. Extract data

# for li in li_list:
#     print(li.prettify())

for li in li_list:
    name = li.h3.a.string
    artist = li.h4.a.string
    options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1 # Tell downloader to download only the first entry (video)
    }
    dl = YoutubeDL(options)
    dl.download([name + artist])



