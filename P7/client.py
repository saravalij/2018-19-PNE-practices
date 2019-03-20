import http.client
import termcolor
import json
import requests
import sys


conn = http.client.HTTPConnection('rest.ensembl.org/')

conn.request("GET", "/")

r1 = conn.getresponse()

print("Response received!: {} {}\n".format(r1.status, r1.reason))

data1 = r1.read().decode("utf-8")

r1.close()

people = json.loads(data1)

print(people)
