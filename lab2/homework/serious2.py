from urllib.request import urlopen 
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
from io import BytesIO

#1. Download trang
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
#1.1 Open a connection to server
conn = urlopen(url)
#1.2 Read data
raw_data = conn.read()
#1.3 Decode data
page_content = raw_data.decode("utf8")


#2. Extract ROI
soup = BeautifulSoup(page_content, "html.parser")
table = soup.find("table",id = "tableContent")
tr_list = table.find_all("tr")


#3. Extract data
ketquahoatdongkinhdoanh = []
for tr in tr_list:
    td_list = tr.find_all("td", "b_r_c")
    for td in td_list:
        td = td.string 
        content = {
            " ": td
        }
        ketquahoatdongkinhdoanh.append(content)

#4. Export
pyexcel.save_as(records=ketquahoatdongkinhdoanh, dest_file_name="serious2.xlsx")

