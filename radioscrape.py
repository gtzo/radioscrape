# GPlay Radio Scraper
# Dumps 25 artist/track names in a radio station
# To use, play the radio station you want to scrape, and 
# then run the script.
# TODO: Sanitize input

import pprint
from gmusicapi import Mobileclient

formatted = {} 
api = Mobileclient()

email = input('Enter login email (enclosed by quotes): ')
pw = input('Enter password (enclosed by quotes): ')
#tr_num = input('Enter how many tracks to retrieve: ')

login_success = api.login(email, pw, Mobileclient.FROM_MAC_ADDRESS) # Should eval to True if successful

if not login_success:
    print "Login unsuccessful."

else:
    stns = api.get_all_stations()
    last_station = stns[-1]
    id = last_station['id']

    tracks = api.get_station_tracks(id) #TODO: # trax

    for t in tracks:
        pprint.pprint(t) 
        formatted[t['artist']] = t['title']

    pprint.pprint(formatted)



    

    

    


