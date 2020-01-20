# YOURLS-PyAPI-Link-Creator
# Created by Wesley Pyburn (TechNobo)
# https://github.com/TcNobo/YOURLS-PyAPI-Link-Creator

import urllib.request
import json
import urllib
from xml.etree import ElementTree as ET
from xmljson import badgerfish as bf
from xml.etree.ElementTree import fromstring
from json import dumps
import clipboard

url = ""
keyword = ""
requestURL = ""
status = ""
message = ""
title = ""
short = ""


url = ""
while url == "":
    url = input("URL to shorten: ")
url = url.replace("&", "%26")

keyword = input("Enter a short link name: ")
if keyword == "":
    keyword = url.split("/")[-1]

requestURL = "https://tcno.co/s/yourls-api.php" \
            + "?signature={YourSecretSignature}" \
            + "&action=shorturl" \
            + "&keyword=" + keyword \
            + "&format=json" \
            + "&url=" + url

root = urllib.request.urlopen(requestURL).read()
#XML: json = json.loads(dumps(bf.data(fromstring(root))))
json = json.loads(root)
print('\n')

try:
    status = json['status']
    message = json['message']
    short = json['shorturl']
    title = json['title']
except:
    print(root)

out = "STATUS:\t\t" + status + "\n" \
    + "MESSAGE:\t" + message + "\n" \
    + "TITLE:\t\t" + title + "\n" \
    + "SHORTURL:\t" + short + "\n"
print(out)

clipboard.copy(short)