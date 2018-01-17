#!/usr/bin/python
import requests
 #import requests library

import json
#import json library

r = requests.get("http://quotes.rest/qod.json")
#make http request

j = r.json()['contents']['quotes'][0]['quote']

print j,"\n","-Vikram Singh"
