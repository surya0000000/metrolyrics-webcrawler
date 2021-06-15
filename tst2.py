import requests
import bs4

resp=requests.get("https://www.metrolyrics.com/ripple-lyrics-grateful-dead.html")
soup=bs4.BeautifulSoup(resp.content,features="html.parser")
tnamelist=soup.find_all("h1")
print(tnamelist)
