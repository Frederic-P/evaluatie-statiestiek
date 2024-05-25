"""
Utilities for basic statistical operations."""

import numpy as np
import pandas as pd
#import random
import matplotlib.pyplot as plt


def outlier_remover(df, column, iqr = 1.5, upper = True, lower = True):
    """ remove the outliers from a given Pandas Dataframe (df)
        in the column defined by column. 

        By default an outlier follows the 1.5 IQR-rule for both upper
        and lower limits. You can override the default behaviour by 
        overriding the default parameters:
        iqr = float (default 1.5)
        upper = bool (default True): If True top outliers will be removed
        lower = bool (default True): If True lower outliers will be removed
    """
    #calculates IQD of column:
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqd = q3 - q1
    #remove upper outliers:
    highbound = q3 + (iqr * iqd) 
    if upper: 
        df = df.query(f"{column} <= {highbound}")
    #delete lower outliers:
    lowbound = q1 - (iqr * iqd) 
    if lower: 
        df = df.query(f"{column} >= {lowbound}")
    #return df
    return df



def square_root_rule_bins(df): 
    """Implementation of the square root rule to calculate the optimal
    amount of bins for a histogram"""
    dfrows = df.shape[0]
    return int(np.ceil(np.sqrt(dfrows)))


def calculate_bins_for_even_k(min, max, max_bins_allowed = 90):
    """
    A good visualisation for the car dataset has easy to interpre
    bins when it comes to pricing, that's why we do not implement 
    the basic Square Root rule to calculate the optimal amount of bins
    in stead. Bins are calculated so that they do not exceed the 
    given parameter (max_bins_allowed (int)). But then they get reduced
    to the point where the distance between two bins is a multiple
    of the variable base_multiple defined in the function body.
    """
    base_multiple = 1000
    #print(min, max)
    #calculates the amount of bins needed to show data in even K increments.
    min = np.floor(int(min)//base_multiple)*base_multiple
    max = np.ceil(int(max)/base_multiple)*base_multiple
    pricerange = max - min
    #in case you only have a single data point!
    if pricerange == 0:
        pricerange = 1
    bins_required = np.ceil(pricerange/base_multiple)
    bin_correction = np.ceil(bins_required/max_bins_allowed)
    #you now know that your bins have a width of bin_correction * base_multiple
    #you need a new min and new max so that min is the highest possible 
    #multiple of bin_correction under the current min
    #and a new max which is the closest multiple of bin_correction *base_multiple
    #to max:
    factor = bin_correction * base_multiple
    new_min = min // factor * factor 
    new_max = (max // factor +1) *factor
    return(int(bins_required/bin_correction)+1, int(bin_correction), new_min, new_max)


def bootstrap(data, rounds):
    """Takes a pandas series as data and makes rounds (n) bootstraps of it
    """
    avgs = []
    resample_length = len(data)
    for _ in range(rounds):
        # Generate a bootstrap sample with replacement
        bootstrap_sample = np.random.choice(data, size=resample_length, replace=True)
        # Calculate the mean of the bootstrap sample
        avg = np.mean(bootstrap_sample)
        # Store the mean of the bootstrap sample
        avgs.append(avg)
    return avgs

def get_bounds_for_ci(data, alpha):
    """
    data is a list of datapoints
    alpha is the significance level expressed as a float between 0 and 1
    returns the confidence interval as a tuple with the boundaries for
    data, for an alpha-significance level.
    i.e. returns the values that contain 1-alpha% of the data in the 
    middlesection of the histogram with alhpa/2 % of the data in the
    left and right tail.
    """
    lower_bound = np.quantile(data, alpha / 2)
    upper_bound = np.quantile(data, 1 - alpha / 2)
    return lower_bound, upper_bound


def moving_mean_for_clt(data, step, simamount, replace):
    """
        Takes four arguments:
        data = flat list of numerical data 
        step = INT the interval to be used in a range 
        simamount = INT the amount of simulations to run
        replace = BOOL should repalcement be used when making subsamples or not

        This function will return a plot with 'simamount' of simulations of an 
        ever growing subsample taken from the 'data' parameter; generating the 
        subsample can be done with or without using 'replace'ment. To speed things
        up you can set a step-amount so that it only generates a simulation for every
        'step' day. 

        In the same plot horizontal line is plotted which represents the mean of 'data'
    """
    for sim in range(simamount):
        subsample_days = []
        subsample_means = []
        for i in range (1, len(data), int(step)):
            #we'll not use replacement for sampling.
            subsample = np.random.choice(data, i, replace=replace)
            subsample_days.append(i)
            subsample_means.append(np.mean(subsample))
        plt.plot(subsample_days, subsample_means, label=f'forecast {sim+1}')
    plt.axhline(np.mean(data), color='orange', linestyle='--', label='Observed Mean')
    #plt.xscale('log')
    plt.xlim(0)
    plt.xlabel('Days in subsample')
    plt.ylabel('Mean of subsample')
    plt.legend()
    extra = ' (with replacement)' if replace else ' (without replacement)'
    title = f'The mean of the subsample {extra} converges to the mean of a larger set as sample size increases.'
    plt.title(title)
    plt.tight_layout()