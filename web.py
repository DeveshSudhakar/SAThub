import requests
from bs4 import BeautifulSoup

def get_links():
    r=requests.get("https://www.meetup.com/cities/in/chennai/tech/")
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    a=soup.find_all("ul",{"class":"searchResults"})[0]
    lis = set([i.attrs['href'] for i in a.find_all("a")[:200]])
    res = list(['<a href ='+i+'>'+i+'<br>'for i in lis])
    return "\n".join(res)
