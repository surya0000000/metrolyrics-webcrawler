import requests
import bs4

resp=requests.get("https://www.metrolyrics.com/grateful-dead-lyrics.html")

soup=bs4.BeautifulSoup(resp.content)

titles
print(resp.content)

