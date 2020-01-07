import requests
from sys import argv
import re
import wget
import pyperclip

url = "https://www.youtube.com/watch?v=sWrqyQWfhrs"

# if argv == 2 :
#     url = argv[1]
# else :
#     url = input("Enter Yotube URL : ")

if(not "http" in url):
    url = "https://" + url

videoId = url.split("watch?v=")[1]

r = requests.get(url)

# with open("fileHTML.txt","wb") as file :
#     file.write(r.text.encode('utf8'))

links = re.findall(r'(https:.+?)\"', r.text)
linksFinal = []
for link in links:
    if("googlevideo.com" in link):
        link = link + '&contentlength=178814912'
        link = link.replace("\\u0026", "&")
        link = link.replace("\\&", "&")
        link = link.replace("\\/", "/")
        linksFinal.append(link)

# videoLink = linksFinal.pop()
videoLink = linksFinal[3]

# videoLink = videoLink + '&contentlength=178814912'
# # videoLink = videoLink + '&' + videoId
# # videoLink = videoLink + '&title='

# videoLink = videoLink.replace("\\u0026", "&")
# videoLink = videoLink.replace("\\&", "&")
# videoLink = videoLink.replace("\\/", "/")

print(videoLink)
# pyperclip.copy(videoLink)

# wget.download(videoLink)
