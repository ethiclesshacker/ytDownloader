import requests
from sys import argv
import re
import urllib.parse


def getFile(url):

    r = requests.get(url)
    title = re.findall(r'\\\"title\\\":\\\"(.+?)\\\"',r.text)[0]
    title = title.split()
    title = "+".join(title)
    links = re.findall(r'(https.+?)\\\"', r.text)
    linksFinal = []
    for link in links:
        if("googlevideo.com" in link):
            try:                    
                link = urllib.parse.unquote(link).encode('latin1').decode('unicode_escape')
                link = link.replace("\\u0026", "&")
                link = link + '&contentlength=178814912'
                link = link + '&title=' + title
            except: 
                continue

            linksFinal.append(link)
            print(link)

    videoLink = linksFinal[3]
    return videoLink



# getFile("https://www.youtube.com/watch?v=30W9txGVZXg")
# videoLink = linksFinal.pop()
# videoLink = videoLink + '&contentlength=178814912'
# # videoLink = videoLink + '&' + videoId
# # videoLink = videoLink + '&title='

# videoLink = videoLink.replace("\\u0026", "&")
# videoLink = videoLink.replace("\\&", "&")
# videoLink = videoLink.replace("\\/", "/")

# print(videoLink)
# pyperclip.copy(videoLink)

# wget.download(videoLink)
