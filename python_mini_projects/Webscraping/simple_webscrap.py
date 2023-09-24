import requests #send req
from bs4 import BeautifulSoup # features content  
url='https://codingnepalweb.com/' 
req = requests.get(url) #response 200
req
soup = BeautifulSoup(req.content, 'html')   
title = soup.find_all('h3',{'class':'entry-title td-module-title'}) 
title
title2 = title[1].getText()
print(title2)
for i in title: #display all titles in the class
    print(i.getText())

#output
#fetch and displays titles

