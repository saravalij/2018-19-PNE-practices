import http.client
import json


HOSTNAME = "www.metaweather.com"
METHOD = 'GET'
headers = {'User-Agent': 'http-client'}

ENDPOINT = "/api/location/search/?query="      # first one!!!!!!!

conn = http.client.HTTPSConnection(HOSTNAME)


notvalid = True
query = ''
try:
    while notvalid:

        query = input('\nPlease enter the capital city you want info from: ')
        query = query.lower().replace(' ', '%20')

        conn.request(METHOD, ENDPOINT + query, None, headers)        # why do i have to delete '/'?????? just bc api format?
        r1 = conn.getresponse()
        text_json = r1.read().decode("utf-8")
        conn.close()
        file = json.loads(text_json)

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

    ENDPOINT = '/api/location/'      # second one!!!!!!!!!!

    conn.request(METHOD, ENDPOINT + LOCATION_WOEID + '/', None, headers)
    r1 = conn.getresponse()
    print()
    print("Response received: ", end='')
    print(r1.status, r1.reason)
    text_json = r1.read().decode("utf-8")
    conn.close()
    file = json.loads(text_json)

    temp = (file['consolidated_weather'][0])['the_temp']

    print('''
    Sought capital city: {}
    Current time: {}
    Temperature: {} degrees
    Sun set time: {}'''.format(query, file['time'], temp, file['sun_set']))

except KeyboardInterrupt:
    print('\nKeyboard interrupter by user.')
