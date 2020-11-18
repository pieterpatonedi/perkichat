#! /usr/bin/env python3
import requests, json
import datetime
import os


token = "iis96ihAcH7wPoTZQpBymGCcz1JTIVSv75USzXWBoYB"# isi token grup buat tes


kalimat = input(">> ")

LINE_ACCESS_TOKEN = token
url = "https://notify-api.line.me/api/notify"
msg = {"message":str(kalimat)} #message
LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
session = requests.Session()
resp =session.post(url, headers=LINE_HEADERS, data=msg)
print(resp.text)

