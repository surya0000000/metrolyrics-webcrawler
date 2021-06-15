import requests
import bs4


def getallsonglinks(url):

	resp=requests.get(url)




	soup=bs4.BeautifulSoup(resp.content,features="html.parser")

	titles=soup.find_all("title")

	links=soup.find_all("a",attrs={"class":"title"})

	for i in links:
	    getsonglyrics(i['href'])

def main():

        getallsonglinks("https://www.metrolyrics.com/grateful-dead-lyrics.html")


def getsonglyrics(url):

        resp=requests.get(url)
        soup=bs4.BeautifulSoup(resp.content,features="html.parser")
        lyrics=soup.find_all("p",attrs={"class":"verse"})
        l=[]
        for i in lyrics:
            l.append(i.get_text())
            
        s="\n".join(l)    
        tnamelist=soup.find("h1")
        tname=tnamelist.get_text()
        tname+=(".txt")
        file=open(tname,"w")
        file.write(s)
        file.close()
        print(tname)

if __name__=="__main__":
        main()


