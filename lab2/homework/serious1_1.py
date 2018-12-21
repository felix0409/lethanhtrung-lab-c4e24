from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

#1. download trang
url = "https://www.apple.com/itunes/charts/songs/"
#1.1 Open a connection to server
conn = urlopen(url)
#1.2 Read data
raw_data = conn.read()
#1.3 Decode data
page_content = raw_data.decode("utf8")


#2. Extract ROI (Region of Interest)
soup = BeautifulSoup(page_content, "html.parser")
section = soup.find("section", "section chart-grid")
div = section.find("div", "section-content")
ul = div.find("ul")
li_list = ul.find_all("li")


#3. Extract data
songs_ranking = []
for li in li_list:
    title = li.h3.a.string
    singer = li.h4.a.string
    link = li.h3.a["href"]
    # print(title)
    # print(link)
    songs = OrderedDict({ 
        "Title": title,
        "Singer": singer,
        "Link": link,
    })
    songs_ranking.append(songs)


#4. Save data to excel
pyexcel.save_as(records=songs_ranking, dest_file_name="songs_ranking_itunes.xlsx")

