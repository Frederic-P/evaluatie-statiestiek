import pandas as pd
import os

"""
basic methods for the cars dataset, focussed on answering the 
questios from the notebook.
"""

#data extraction: 
def extract_brand(df, brandname):
    """
    Extracts the data of a given Brand from the cars dataset.
    """
    brand_data = df[df['manufacturer'] == brandname]
    return brand_data


#numerical operations: 
def get_median_of_column(dataset, column): 
    """
    returns the median for a given column from a pandas dataframe
    """
    return dataset[column].median()

def get_mean_of_column(dataset, column):
    """
    returns the mean for a given column from a pandas dataframe
    """
    return dataset[column].mean()

def get_max_of_column(dataset, column):
    """
    returns the max for a given column from a pandas dataframe
    """
    return dataset[column].max()

def get_min_of_column(dataset, column):
    """
    returns the min for a given column from a pandas dataframe
    """
    return dataset[column].min()

def load_data(filepath): 
    """
        Takes an os.path object to a csv file, 
        reads it into memory and returns it as a pandass dataframe.
    """
    #check if file exists: 
    if(not os.path.exists(filepath)): 
        raise  Exception(
            "Your configurationfile mentions a non-existing dataset.\
            Check if the file exists and is refrerenced correctly."
            )
    #load with pandas and return it to the notebook.
    return pd.read_csv(filepath)


def get_pricegroup(price): 
    """returns an integer which represents the upper price bracket
    per 1000 increments. A car costing 900 will return as 1. """
    return price // 1000 + 1