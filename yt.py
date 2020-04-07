import requests
import re
import json
import urllib.parse


class Youtube:
    def __init__(self,URL):
        self.URL = URL
        self.r = requests.get(URL)

    def getTitle(self): 
        title = re.findall(r'\\\"title\\\":\\\"(.+?)\\\"',self.r.text)[0]
        title = title.split()
        self.title = "+".join(title)

    def getLinks(self):
        
        self.getTitle()
        adaptiveFormats = re.findall(r'\\"adaptiveFormats\\":\[([\s\S]+?)\]',self.r.text)[0]
        adaptiveFormats = adaptiveFormats.replace('\\"','"')
        adaptiveFormats = adaptiveFormats.replace('\\"','"')
        adaptiveFormats = "[" + adaptiveFormats + "]"
        adaptiveFormats = json.loads(adaptiveFormats)
       
        formats = re.findall(r'\\"formats\\":\[([\s\S]+?)\]',self.r.text)[0]
        formats = formats.replace('\\"','"')
        formats = formats.replace('\\"','"')
        formats = "[" + formats + "]"
        formats = json.loads(formats)

        allFormats = formats + adaptiveFormats

        urls = []
        for i in allFormats:
            url = urllib.parse.unquote(i.get("url","")).encode('latin1').decode('unicode_escape')
            url = url + '&contentlength=' + i.get("contentLength","55656757")
            url = url + '&title=' + self.title
            urls.append(url)

        links = {}
        for i,format in enumerate(allFormats):
            if "mp4a" in format.get("mimeType",""):
                links[format.get("qualityLabel","Audio")] = urls[i]

        return links


