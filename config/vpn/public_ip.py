#!/usr/bin/python2

import requests, json, time
import sys

CONFIG_FILE = '/home/icebox/.config/public_ip.data'
UPDATE_EVERY = 60       # seconds

def write_data(js):
    countryCode = js[1]['countryCode']
    city = js[1]['city']
    if len(city) > 12: city = '{}...'.format(city[:12].strip())
    with open(CONFIG_FILE, 'w') as f:
        f.write(js[0] + '\n')
        f.write('{}, {}'.format(city, countryCode))

def update():
    # get IP
    ip = None   # we might have internet connection down
    try:
        r = requests.get('https://api.ipify.org?format=json')
        ip = json.loads(r.text)['ip']
    except: pass
    # if we haven't got any IP, return here
    if not ip: write_data(['N/A', 'N/A'])

    # get location
    location = None
    try:
        r = requests.get('http://ip-api.com/json')
        location = json.loads(r.text)
    except: location = 'N/A'    # something went wrong with location check
    write_data([ip, location])    # write data to file

def main():
    forever = False
    if sys.argv[-1].strip().lower() == 'forever': forever = True
    while True:
        try:
            update()
            print '[+] updated !'
            # if it's not forever, return here
            if not forever: return
            time.sleep(UPDATE_EVERY)
        except Exception, ex:
            print '[-] error: {}'.format(ex)
            time.sleep(10)      # retry in 10 seconds
main()
