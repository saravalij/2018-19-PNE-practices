# The maximum I get is 30, due to the rate limit GitHub applies.

import http.client
import json

def get_json(ENDPOINT):

    conn.request('GET', ENDPOINT, None, {'User-Agent': 'http-client'})

    r1 = conn.getresponse()

    text_json = r1.read().decode("utf-8")
    conn.close()

    return json.loads(text_json)


HOSTNAME = "api.github.com"

conn = http.client.HTTPSConnection(HOSTNAME)

notvalid = True

try:
    while notvalid:
        git_id = input('\nPlease introduce the username of the github profile you want to have info about: ')
        user = get_json('/users/' + git_id)

        if len(user) == 31:
            notvalid = False
        else:
            print('\nSorry, we could not find that username in our database. Try again.')

    git_id = user['login']

    repos = get_json('/users/{}/repos'.format(git_id))
    commits = get_json('/repos/{}/2018-19-PNE-practices/commits'.format(git_id))
    rep_names = []
    total_c = ''

    for r in repos:
        rep_names.append(r['name'])

    rep_names = ', '.join(rep_names)

    if type(commits) != list:
        total_c = "0 ! INEXISTENT REPO"
    else:
        total_c = len(commits)

    print('''
    User: {}
    Name: {}
    Repos: {}
    Commits to 2018-19-PNE-repo: {}'''.format(git_id, user['name'], rep_names, total_c))

except KeyboardInterrupt:
    print()
    print('\nKeyboard interrupted by the user.')
