"""
    This file is the declaration of the Tweet class
    @author: Patrick Brzezina, University of North Texas 11398682
    
    to run: python3 Analyze_Tweets.py 
"""

class Tweet:
    # Constructor for this class
    def __init__(self, msg, polarity_score):
        self.msg = msg
        self.polarity_score = polarity_score
        self.sentiment = self.eval_sentiment (self.polarity_score)
    
    # Helper function used to find sentiment based on the given polarity score   
    def eval_sentiment (self, polarity_score):
        if polarity_score > 0:
            return 'positive'
        elif polarity_score == 0:
            return 'neutral'
        else:
            return 'negative'
    
    # Function used to get polarity score
    def get_polarity_score (self):
        return self.polarity_score
    
    # Function used to get text of the tweet
    def get_msg (self):
        return self.msg
    
    # Function used to get sentiment
    def get_sentiment (self):
        return self.sentiment