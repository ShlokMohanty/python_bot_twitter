import time 
import datetime
import random 
from os import environ
import dropbox
import requests 
import urlib.request 
import os
from musixmatch_api_cleaner import *

import tweepy 

key = environ['TWITTER_KEY']
secret = environ['TWITTER_SECRET']
BearerToken = environ['TWITTER_BearerToken']
access_token = environ['TWITTER_access_token']
access_token_secret = environ['TWITTER_access_token_secret']
api_key = environ['UNPLASH_api_key']
DB_Token = environ['Dropbox_Token']

dbx = dropbox.Dropbox(DB_Token)
auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token(access_token, access_token_secret)
