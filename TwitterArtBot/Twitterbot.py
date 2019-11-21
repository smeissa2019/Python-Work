
import tweepy
from time import sleep

import os

cwd = os.getcwd() 
files = os.listdir(cwd)  
print("Files in %r: %s" % (cwd, files))
my_file = open(r"C:\Users\sa418774\Documents\Python work\TwitterArtBot\verne.txt", "r", encoding="utf8")
file_lines = my_file.readlines()
my_file.close()

consumer_key = 'HXJwIytG3G6L8d7MAbmuVkbR7'
consumer_secret = 'yGgw1oJ43EutwInSPifn9U2k4FAIrwrYu82hJzI2OR7wsoaBFK'
access_token = '1194456102529904640-TszAakWUWgP4rzBB0pQZPsMJl9KOok'
access_token_secret = '7DHlXD5gTzV9GCzxZZ4DklPUwoHBt8upELxT7QykFray4'

auth =tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

def tweets():
   for line in file_lines:
       try:
           if line != '\n':
               line1 = print(line)
               tweet = (line1, id(line))
               id(line) +1
               api.update_status(status=tweet)
               sleep(900)
               
           else:
                pass
       except tweepy.TweepError as error:
           if error.api_code ==187:
              print(error.reason)
              sleep(2)

tweets()