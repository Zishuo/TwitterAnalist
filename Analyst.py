import sys
from NLP import *
from DB import *
from GEO import *
import time
def main(argv):
    db = DBO()
    nlp = NLPEngine()
    maps = GEO()

    table_tweets = Tweets(db)
    table_locations = Locations(db)
    places = table_tweets.get_place()
    for place in places:
        (p,) = place
        cordinate = maps.geocode(p)
        if cordinate is not None:
            table_locations.insert(p,cordinate['lat'],cordinate['lng']) 
    
#    tweets = table_tweets.get_tweets_wo_place()
#    for tweet in tweets:
#        TWTID = tweet[0]
#        text = tweet[5]
#        score = nlp.sentiment(text)
#        place = nlp.place(text)
#        table_tweets.update_sentiment(TWTID, score)
#        if place is not None:
#            table_tweets.update_place(TWTID, place)
        
if __name__ == "__main__":
    main(sys.argv)
