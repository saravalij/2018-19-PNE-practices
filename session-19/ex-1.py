import http.client
import json

# -- API information
HOSTNAME = "api.icndb.com"
ENDPOINT = ["/jokes/count", '/categories', '/jokes/random']
GITHUB_ID = "Obijuan"
METHOD = "GET"

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection(HOSTNAME)

total = 0
cat_num = 0
cat_li = []
joke = ''


for i in ENDPOINT:

    conn.request(METHOD, i, None, headers)

    # -- Wait for the server's response
    r1 = conn.getresponse()

    text_json = r1.read().decode("utf-8")
    conn.close()

    data = json.loads(text_json)

    if 'count' in i:
        total = data['value']
    elif 'categories' in i:
        cat_li = data['value']
        cat_num = len(cat_li)
    elif 'random' in i:
        joke = (data['value'])['joke']
    else:
        print('error macho')


print('''\nTotal number of jokes in the database: {}
Total number of jokes categories: {}
Names of all jokes categories: {}
Random joke for you: {}'''.format(total, cat_num, cat_li, joke))
