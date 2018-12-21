from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel #as p
from collections import OrderedDict

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

# print(songs_ranking)


# #4. Save data to excel
# pyexcel.save_as(records=songs_ranking, dest_file_name="songs_ranking_itunes.xlsx")

