#!C:\Users\Seokhawn\anaconda3\python
import sys
import codecs
import cgi, os
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach()) # 한글 출력을 위한 Encoding

form = cgi.FieldStorage()
pageId = form["pageId"].value
title = form["title"].value
description = form["description"].value

file = open('data/'+pageId, 'w', encoding='utf-8')
file.write(description)
file.close()
os.rename('data/'+pageId, 'data/'+ title)

#Redirection - 사용자를 웹서버가 다른 page로 보내버리는 것
print("Location: index.py?id="+title) #print pay load
print() # print endline
