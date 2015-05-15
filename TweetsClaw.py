from TwitterSearch import *
class TweetSearch:
    def __init__(self):
        self.ts = TwitterSearch(
                consumer_key = 'zTY2l3OYf9n50WgPG6KOCcr3J',
                consumer_secret = 'sHqr1o1bCmW5xqPQE6wA7wCwsti00kT6hDnM6SlHNIr2kqStiJ', 
                access_token = '597976696-zDOpw9mCLkJ05JKXemq9OAJ1qf6pjVg0G4zhtCrl',
                access_token_secret = 'lmiwWH69u5MfDGWNhXaFlcyo4882uN2Fm7dYxcAPVPaAq')

    def search(self,keywords):
        tso = TwitterSearchOrder()
        tso.set_keywords(keywords)
        tso.set_language('en')
        tso.set_include_entities(False)
        try:
            tweets = self.ts.search_tweets_iterable(tso)
        except TwitterSearchException as e: # catch all those ugly errors
            print(e)
        return tweets
