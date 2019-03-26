import http.client
import json


def get_json(ENDPOINT, s):
    HOSTNAME = "www.metaweather.com"
    conn = http.client.HTTPSConnection(HOSTNAME)

    conn.request('GET', ENDPOINT + s + '/', None, {'User-Agent': 'http-client'})

    r1 = conn.getresponse()

    text_json = r1.read().decode("utf-8")
    conn.close()

    file = json.loads(text_json)

    return file

# ENDPOINT = "/api/location/search/?query="


notvalid = True


while notvalid:
    query = input('Please enter the capital city you want info from: ')
    query = query.lower()
    file = get_json("/api/location/search/?query=", query)
    if len(file) == 1:
        notvalid = False

LOCATION_WOEID = file['woeid']

file = get_json(LOCATION_WOEID)

temp0 = file['consolidated_weather'][0]
temp = temp0['the_temp']

print('''\nSought capital city: {}
Current time: {}
Temperature: {}
Sun set time: {}'''.format(query, file['time'], temp, file['sun_set']))
