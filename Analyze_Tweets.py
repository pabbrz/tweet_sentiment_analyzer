"""
    This file reads in and stores all the tweets for further analysis.
    The software first assigns polarity scores and sentiments to each tweet by creating tweet objects (see Tweet.py)
    Afterwards the results of computations of basic stats, data spreads, and probability mass functions are stored in output text files
    
    @author: Patrick Brzezina, University of North Texas 11398682
    
    to run: python3 Analyze_Tweets.py 
"""

import csv
from textblob import TextBlob
import Data_Analysis_Tools as dat
from Tweet import Tweet

# Helper function used to read and categorize tweets
def read_tweets(filename):
    # Initialize empty lists for storage
    tweet_polarity = []
    positive_scores = []
    negative_scores = []
    neutral_scores = []
    tweets = []
    
    # Open the input CSV file
    with open(filename, 'r') as input_file:
        # Create a CSV reader object
        reader = csv.reader(input_file)

        # Open the output CSV file
        with open('output.csv', 'w', newline='') as output_file:
            # Create a CSV writer object
            writer = csv.writer(output_file)

            # Iterate over the rows in the input CSV file
            for row in reader:
                # Get the string from the first column of the row
                msg = row[0]

                # Use TextBlob to evaluate the sentiment of the string
                sentiment_score = TextBlob(msg).sentiment.polarity
                t = Tweet(msg, sentiment_score)
                tweets.append(t)
                sentiment = t.get_sentiment()
                
                # Add sentiment polarity score for current tweet to corresponding list
                if sentiment_score > 0:
                    positive_scores.append(sentiment_score)
                elif sentiment_score == 0:
                    neutral_scores.append(sentiment_score)
                else:
                    negative_scores.append(sentiment_score)

                # Write the original row and the sentiment to the output CSV file
                writer.writerow(row + [sentiment_score] + [sentiment])
            
            # Save lists inside one bigger one to return
            tweet_polarity.append(positive_scores)
            tweet_polarity.append(negative_scores)
            tweet_polarity.append(neutral_scores)
            tweet_polarity.append(tweets)
        
        # Return list containing categorized tweet polarity            
        return tweet_polarity
    
    

    

def main ():
    # Read in and categorize tweets
    polarity_list = read_tweets('tweets_1000.csv')
    
    # Save category names for each list type, used later to create axes in bar charts
    polarity_categories = ['Positive', 'Negative', 'Neutral']
    deviation_categories = ['one std. dev.', 'two std. dev.', 'outliers']
    
    # Generates and saves basic stats
    stats_list = dat.generate_basic_stats(polarity_list, 'Basic_Stats.txt')
    
    
    # Generate lists of different types of data for each sentiment category based on empirical rule
    total_dev_counts = dat.find_dev_counts (dat.find_all_scores(polarity_list), stats_list[0][0], stats_list[0][1]) 
    positive_dev_counts = dat.find_dev_counts (polarity_list[0], stats_list[1][0], stats_list[1][1]) 
    negative_dev_counts = dat.find_dev_counts (polarity_list[1], stats_list[2][0], stats_list[2][1])
    
    # Generate Bar chart representing the comparison of the number of tweets in each category
    dat.generate_category_bar_chart (polarity_list, 'category_count_comparison.jpg', polarity_categories)
    
    # Generate bar charts comparing the number of each classifications of deviations in each category
    dat.generate_category_bar_chart (positive_dev_counts, 'positive_data_type_count_comparison.jpg', deviation_categories)
    dat.generate_category_bar_chart (negative_dev_counts, 'negative_data_type_count_comparison.jpg', deviation_categories)
    dat.generate_category_bar_chart (total_dev_counts, 'total_data_type_count_comparison.jpg', deviation_categories)
    
    
    # Generate trend lines for different categories of data
    dat.generate_trend_line(polarity_list[0], 'orange', 'positive_tweets_trend.jpg')
    dat.generate_trend_line(polarity_list[1], 'red', 'negative_tweets_trend.jpg')
    dat.generate_trend_line(polarity_list[2], 'green', 'neutral_tweets_trend.jpg')
    
    # Generate PMFs for each category of sentiment
    dat.generate_pmf_models (polarity_list, 'PMF_Models_Per_Category.txt')
    
    
    
if __name__ == '__main__':
    main()
    