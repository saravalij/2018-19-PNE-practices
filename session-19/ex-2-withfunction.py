import http.client
import json


def get_json(ENDPOINT, s):

    conn.request('GET', ENDPOINT + s, None, {'User-Agent': 'http-client'})

    r1 = conn.getresponse()

    text_json = r1.read().decode("utf-8")
    conn.close()

    return json.loads(text_json)


HOSTNAME = "www.metaweather.com"
notvalid = True
query = ''

conn = http.client.HTTPSConnection(HOSTNAME)

try:
    while notvalid:

        query = input('\nPlease enter the capital city you want info from: ')
        query = query.lower().replace(' ', '%20')

        file = get_json("/api/location/search/?query=", query)

        if len(file) == 1:
            query = file[0]['title']
            LOCATION_WOEID = str(file[0]['woeid'])
            notvalid = False
        else:
            options = []
            for i in file:
                options.append(i['title'])
            print('\nYou must introduce a valid capital city...')
            if len(options) > 0:
                print('Maybe you meant {}?'.format(', '.join(options)))

    file = get_json('/api/location/', LOCATION_WOEID + '/')

    temp = (file['consolidated_weather'][0])['the_temp']

    print('''
    Sought capital city: {}
    Current time: {}
    Temperature: {} degrees
    Sun set time: {}'''.format(query, file['time'], temp, file['sun_set']))

except KeyboardInterrupt:
    print('Keyboard interrupted by user.')
