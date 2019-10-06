import requests
from gtts import gTTS
import os

r=requests.get("https://kiss-novel.com/ancient-godly-monarch/chapter-2")


from bs4 import BeautifulSoup
soup=BeautifulSoup(r.text,'html.parser')
results=soup.find_all('div',attrs={'id':'content'})
first_result=results[0]
alltext=first_result.contents
n=len(alltext)
for i in range(n):
    alltext[i]=str(alltext[i])
for i in range(len(alltext)):
    if(alltext[i]=='<br/>'):
        alltext.pop(i)
        alltext.insert(i,"\n")
n=len(alltext)
fp=open("new.txt","w")
for i in range(n):
    fp.write(alltext[i])
fp.close()
f=open("new.txt")
x=f.read()
print("This takes sometime to create ur mp3 file please wait.....")
op = gTTS(text=x,lang='en',slow=False)
op.save("op.mp3")
os.system("start op.mp3")
os.remove("op.mp3")

