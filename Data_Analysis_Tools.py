"""
    This file creates various functions and tools for use with various analysis of tweet data.
    
    @author: Patrick Brzezina, University of North Texas 11398682 
"""

import numpy as np
import matplotlib.pyplot as plt
import math


# Generates a scatterplot and trend line with a list 
def generate_trend_line(polarity_list, color, filename):
    # Intialize list and populate it to represent the key of each tweet
    tweet_num = generate_tweet_nums (polarity_list)
    
    # Save each list 
    x = np.array(tweet_num)
    y = np.array(polarity_list)    
    
    #create scatterplot
    plt.scatter(x, y)

    #calculate equation for quadratic trendline
    z = np.polyfit(x, y, 2)
    p = np.poly1d(z)

    #add trendline to plot
    plt.plot(x, p(x), color=color, linewidth=3, linestyle="--")

    # Saving the figure.
    plt.savefig(filename)
    
    # Clear for next use
    plt.clf()


# Generate a seperate integer array representing each tweet index
def generate_tweet_nums (list):
    # Intialize list and populate it to represent the key of each tweet
    tweet_num = []   
    
    # Populate array with each index
    for i in range(len(list)):
        tweet_num.append(i)
    
    # Return populated array
    return tweet_num

# Generate an list of all polarity scores combined
def find_all_scores (polarity_list):
    # Intialize list and populate it to represent the key of each tweet
    all_scores = []
    
    for i in polarity_list[3]:
        all_scores.append(i.get_polarity_score())
    
    # Return populated list of all scores
    return all_scores

# Finds and returns first occurence of a given sentiment
def find_first_occurence (list, sentiment):
  # Set up variable to keep track of all occurences traversed over
  count = 0
  
  # Iterate thru list and count all indexes traversed before first intance of given sentiment is found
  for i in list:
    if i.get_sentiment() == sentiment:
      return count
    count += 1
      


# Defines a function that generates a bar chart and saves it to a file
def generate_category_bar_chart (list, filename, categories):
  # Set the categories and counts for the bar chart
  category_counts = [len(list[0]), len(list[1]), len(list[2])]
  
  # Generate the bar chart
  plt.bar(categories, category_counts)
  
  # Save the bar chart to the specified file
  plt.savefig (filename)
  
  # Reset figure for next use
  plt.clf()


# Defines a function that generates a bar chart and saves it to a file
def generate_stat_category_bar_chart (dev_counts_list, filename, categories):
  
  # Generate the bar chart
  plt.bar(categories, dev_counts_list)
  
  # Save the bar chart to the specified file
  plt.savefig (filename)
  
  # Reset figure for next use
  plt.clf()


# Defines a function that calculates the mean of a list of numbers
def find_mean (list):
  # Initialize the average to 0
  avg = 0
  
  # Add up all the values in the list
  for i in list:
    avg += i
  
  # Return the average by dividing the sum by the number of values
  return avg / len(list)


# Defines a function that calculates the standard deviation of a list of numbers
def find_std_dev (list, mean):
  # Initialize the standard deviation to 0
  std_dev = 0
  
  # Calculate the standard deviation
  for i in list:
    std_dev += pow((i - mean), 2)
  
  # Divide by the number of values - 1 to get the unbiased estimate of the standard deviation
  std_dev /= (len(list) - 1)
  
  # Return the standard deviation
  return std_dev


# Defines a function that generates basic statistics for a list of polarity scores
def generate_basic_stats (polarity_list, filename):
  stats_list = []
  total_stats = []
  positive_stats = []
  negative_stats = []
  neutral_stats = []
  
  
  # Open the output file for writing
  with open(filename, 'w') as of:
    
    # If the output file could not be opened, print an error message and return
    if of == None:
      print ('Error opening output file ' + str(filename) + ' for basic statistics.')
      return
    
    # Create a list of all the polarity scores
    scores = []
    for i in polarity_list[3]:
      scores.append(i.get_polarity_score())
    
    # Calculate the mean and standard deviation of all the scores and store in list
    total_avg_score = find_mean (scores)
    total_stats.append(total_avg_score)
    total_std_dev = find_std_dev (scores, total_avg_score)
    total_stats.append(total_std_dev)
    
    # Add list of total stats to list of all stats
    stats_list.append(total_stats)
    
    
    # Write the mean and standard deviation to the output file
    of.write('Average Polarity Rating of all Tweets is: ' + str(total_avg_score) + '\n')
    of.write('Standard Deviation of Polarity Ratings of all Tweets is: ' + str(total_std_dev) + '\n\n')
    
    # Calculate the mean and standard deviation of the positive scores
    positive_avg_score = find_mean (polarity_list[0])
    positive_stats.append(positive_avg_score)
    positive_std_dev = find_std_dev (polarity_list[0], positive_avg_score)
    positive_stats.append(positive_std_dev)
    
    # Add list of positive stats to list of all stats
    stats_list.append(positive_stats)
    
    # Write the mean and standard deviation of the positive scores to the output file
    of.write('Average Polarity Rating of all Positive Tweets is: ' + str(positive_avg_score) + '\n')
    of.write('Standard Deviation of Polarity Ratings of all Positive Tweets is: ' + str(positive_std_dev) + '\n\n')

    # Calculate the mean and standard deviation of the negative scores
    negative_avg_score = find_mean (polarity_list[1])
    negative_stats.append(negative_avg_score)
    negative_std_dev = find_std_dev (polarity_list[1], negative_avg_score)
    negative_stats.append(negative_std_dev)
    
    # Add list of positive stats to list of all stats
    stats_list.append(negative_stats)
    
    # Write the mean and standard deviation of the negative scores to the output file
    of.write('Average Polarity Rating of all Negative Tweets is: ' + str(negative_avg_score) + '\n')
    of.write('Standard Deviation of Polarity Ratings of all Negative Tweets is: ' + str(negative_std_dev) + '\n\n')
    
    # Calculate the mean and standard deviation of the neeutral scores
    neutral_avg_score = find_mean (polarity_list[2])
    neutral_stats.append(neutral_avg_score)
    neutral_std_dev = find_std_dev (polarity_list[2], neutral_avg_score)
    neutral_stats.append(neutral_std_dev)
    
    # Add list of positive stats to list of all stats
    stats_list.append(neutral_stats)
    
    # Write the mean and standard deviation to the output file
    of.write('Average Polarity Rating of all Neutral Tweets is: ' + str(neutral_avg_score) + '\n')
    of.write('Standard Deviation of Polarity Ratings of all Neutral Tweets is: ' + str(neutral_std_dev) + '\n\n')
    
    # Close output file for no more further reading
    of.close()
    
    return stats_list
        
        
# Defines a function that finds the number of values in a list that fall within certain ranges
def find_dev_counts (list, std_dev, mean):
  # Initialize lists to store the values that fall within certain ranges
  dev_counts_list = []
  one_std_dev = []
  two_std_dev = []
  outliers = []
  
  # Iterate over the values in the list
  for i in list:
    is_outside_one = (i < (mean - std_dev) or i > (mean + std_dev))
    is_outside_two = i < (mean - (2 * std_dev)) or i > (mean + (2 * std_dev))
    is_outside_three = i < (mean - (3 * std_dev)) or i > (mean + (3 * std_dev))  
      
    # If the value is outside the range of greater than one standard deviation from the mean, add it to the one_std_dev list
    if is_outside_one and not is_outside_two and not is_outside_three:
      one_std_dev.append(i)
      
    # If the value is outside the range of greater than two standard deviations from the mean, add it to the two_std_dev list
    elif is_outside_two and not is_outside_three:
      two_std_dev.append(i)
      
    # If the value is outside the range of greater than three standard deviations from the mean, add it to the outliers list
    elif is_outside_three:
      outliers.append(i)
      
    # If the value is within the range of one, two, or three standard deviations from the mean, do nothing
    else:
      pass
  
  # Add the lists of values to the dev_counts_list and return it
  dev_counts_list.append (one_std_dev)
  dev_counts_list.append (two_std_dev)
  dev_counts_list.append(outliers)
  
  return dev_counts_list

    
# Evaluates and returns the bernoulli probability mass function evaluation of a given list, probability, and sentiment to look for
def bernoulli_pmf(tweets, n, k, sentiment):
    # Set number of tweets matching intially to 0
    n_matching = 0
    p = n / k

    # Iterate thru and calculate the number of matching tweets to the sentiment type
    for i in tweets:
        if i.get_sentiment() == sentiment:
            n_matching += 1
        
    # Calculate and return the bernoulli pmf probability 
    return p ** n_matching * (1 - p) ** (len(tweets) - n_matching)


# Evaluates and returns the binomial probability mass function evaluation of a given proportion and probability
def binomial_pmf(n, k, p):
  return (math.factorial(n) / (math.factorial(k) * math.factorial(n-k))) * p**k * (1 - p)**(n-k)


# Finds and returns the probability mass function evaluations of a given probability and number of total strings
def geometric_pmf(n, k, z):
  p = n / k
  return p * (1 - p)**(z-1)

# Calculate and write PMFs for each category of polarity score
def generate_pmf_models (polarity_list, filename):    
    # Store total number of list
    size = len(polarity_list[3])
    
    # Open the output file for writing
    with open(filename, 'w') as of:
        # Find bernoulli pmf model evaluations of positive, negative, and neutral tweets
        positive_bern_pmf = bernoulli_pmf (polarity_list[3], len(polarity_list[0]), size, 'positive')
        negative_bern_pmf = bernoulli_pmf (polarity_list[3], len(polarity_list[1]), size, 'negative')
        neutral_bern_pmf = bernoulli_pmf (polarity_list[3], len(polarity_list[2]), size, 'neutral')
        
        # Find binomial pmf model evaluations of positive, negative, and neutral tweets
        positive_bin_pmf = binomial_pmf (size, len(polarity_list[0]), len(polarity_list[0]) / size)
        negative_bin_pmf = binomial_pmf (size, len(polarity_list[1]), len(polarity_list[1]) / size)
        neutral_bin_pmf = binomial_pmf (size, len(polarity_list[2]), len(polarity_list[2]) / size)
        
        # Find geometric pmf model evaluations of positive, negative, and neutral tweets
        positive_geo_pmf = geometric_pmf (len(polarity_list[0]), size, find_first_occurence(polarity_list[3], 'positive'))
        negative_geo_pmf = geometric_pmf (len(polarity_list[1]), size, find_first_occurence(polarity_list[3], 'negative'))
        neutral_geo_pmf = geometric_pmf (len(polarity_list[2]), size, find_first_occurence(polarity_list[3], 'neutral'))
        
        # Write PMFs for positive polarity score to output file
        of.write ('Bernoulli Distribution Probability Mass Function Evaluation for Positive Polarity Score: ' + str (positive_bern_pmf) + '\n')
        of.write ('Binomial Distribution Probability Mass Function Evaluation for Positive Polarity Score: ' + str (positive_bin_pmf) + '\n')
        of.write ('Geometric Distribution Probability Mass Function Evaluation for Positive Polarity Score: ' + str (positive_geo_pmf) + '\n\n')
        
        # Write PMFs for negative polarity score to output file
        of.write ('Bernoulli Distribution Probability Mass Function Evaluation for Negative Polarity Score: ' + str (negative_bern_pmf) + '\n')
        of.write ('Binomial Distribution Probability Mass Function Evaluation for Negative Polarity Score: ' + str (negative_bin_pmf) + '\n')
        of.write ('Geometric Distribution Probability Mass Function Evaluation for Negative Polarity Score: ' + str (negative_geo_pmf) + '\n\n')
        
        # Write PMFs for neutral polarity score to output file
        of.write ('Bernoulli Distribution Probability Mass Function Evaluation for Neutral Polarity Score: ' + str (neutral_bern_pmf) + '\n')
        of.write ('Binomial Distribution Probability Mass Function Evaluation for Neutral Polarity Score: ' + str (neutral_bin_pmf) + '\n')
        of.write ('Geometric Distribution Probability Mass Function Evaluation for Neutral Polarity Score: ' + str (neutral_geo_pmf) + '\n\n')
        
        
        
        
        
    

    
    