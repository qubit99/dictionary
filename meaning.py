from bs4 import BeautifulSoup
import urllib.request
import time
"This program finds the meaning of word"
word=input('enter the word: ')
website='https://dictionary.cambridge.org/dictionary/english/'+word

req=urllib.request.Request(website)
with urllib.request.urlopen(req) as response:
    the_page=response.read()

soup = BeautifulSoup(the_page, 'html.parser')
source=soup.prettify()
for i in range(len(source)):
    if source[i:i+10]=="Learn more":
        high=i
        break
low=264 + 2*len(word)
source=source[low:high]
k=str(source).split(":")
k.pop()
for j in k:
    print(j)
time.sleep(100)
