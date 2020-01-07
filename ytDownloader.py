import requests
from sys import argv
import re


# if argv == 2 :
#     url = argv[1]
# else :
#     url = input("Enter Yotube URL : ")

# if(not "http" in url):
#     url = "https://" + url

# videoId = url.split("watch?v=")[1]

def getFile(url):

    r = requests.get(url)
    title = re.findall(r'\\\"title\\\":\\\"(.+?)\\\"',r.text)[0]
    title = title.split()
    title = "+".join(title)
    print(title)
    links = re.findall(r'(https:.+?)\"', r.text)
    linksFinal = []
    for link in links:
        if("googlevideo.com" in link):
            link = link + '&contentlength=178814912'
            link = link + '&title=' + title
            link = link.replace("\\u0026", "&")
            link = link.replace("\\&", "&")
            link = link.replace("\\/", "/")
            linksFinal.append(link)

    videoLink = linksFinal[3]
    return videoLink





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
