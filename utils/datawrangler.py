import pandas as pd
import os


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