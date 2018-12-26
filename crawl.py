import time
import sys
import os
import argparse
import codecs
import tweepy
import json
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

 
consumer_key = 'roVBZrfN1tt0Wbtnl98rAJBjv'
consumer_secret = 'LhRHZhqDwzyaoK4RIJbjOdtSm5EqrQ0EaTh7WifeOQ8izB89lk'
access_token = '1058836266127511552-ujuXvzAKH3JNwNpJvw2wnYH3zGqWJI'
access_secret = 'hpKjEKMaFqGm8ltlMoW772L6dAengOJVxTIiLEVlkIFXt'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth, wait_on_rate_limit=True,
                       wait_on_rate_limit_notify=True)

# candidates = ["AubichonMaynard","LetsFixHousing","gzlfb","Drpingchan","DavidChenTweets","Drpingchan",
#               "vancitycrime","Realfredharding","rollergirl2014","sshottha",
#               "kensimformayor","kennedystewart","ShaunaSylvester","johnmyano","WaiYoung"]
candidates = ["ShaunaSylvester","johnmyano","WaiYoung"]

def twitter_miner(outfile, outfile1):                           #using the mining function to crawling tweets
        try:

            api = tweepy.API(auth)

            max_tweets = 5000
            newTweets = [status for status in tweepy.Cursor(api.user_timeline, tweet_mode='extended', id=candidate, since= "2017-10-20 08:30", 
                                                            until= "2018-10-20 08:30" ).items(max_tweets)]   #crawling 5000 new tweets

            for tweet in newTweets:
                #print(tweet)
                if (not tweet.retweeted) and ('RT @' not in tweet.full_text):
                    str1=str((tweet.full_text).replace('\n', ' ').encode('utf-8').lower())
                    outfile.write(str1 + "\n")
                    str2=str(str(tweet.id).encode('utf-8') + ' '.encode('utf-8') + tweet.user.name.encode('utf-8') + 
                             ' '.encode('utf-8') + tweet.user.screen_name.encode('utf-8') +
                             ' '.encode('utf-8') + (tweet.full_text).replace('\n', ' ').encode('utf-8')).lower()

                    outfile1.write(str2+"\n")        #Write the tweet.id, username, tweeter content to output1.txt

        except tweepy.TweepError as e:
            print("some error : " + str(e))
            print("retrying in 20 seconds")
            time.sleep(20)
        #continue
for candidate in candidates:
    filename = candidate+".txt"
    filename1 = candidate+"1.txt"
    outfile=open(filename,"a")    #Write the content of tweet to output.txt
    outfile1=open(filename1,"a")
    twitter_miner(outfile, outfile1)
    outfile.close()
    outfile1.close()
    