import numpy as np

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

