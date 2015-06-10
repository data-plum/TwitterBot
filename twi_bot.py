#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys
 
argfile = str(sys.argv[1])
 
CONSUMER_KEY = '' #your consumer key
CONSUMER_SECRET = '' #your consumer secret key
ACCESS_KEY = '' #your access token
ACCESS_SECRET = '' #your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
filename = open(argfile,'r')
f = filename.readlines()
filename.close()
 
for line in f:
	api.update_status(status = line)
	time.sleep(300)