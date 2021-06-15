

import requests
import bs4

resp=requests.get("https://www.metrolyrics.com/ripple-lyrics-grateful-dead.html")
soup=bs4.BeautifulSoup(resp.content,features="html.parser")
lyrics=soup.find_all("p",attrs={"class":"verse"})
l=[]
for i in lyrics:
   l.append(i.get_text())
s="\n".join(l)
f=open("example.txt","w")
f.write(s)
f.close()
tnamelist=soup.find_all("h1",attrs={"class":"banner-heading"})

print(tnamelist)
#tname=tnamelist[0]
