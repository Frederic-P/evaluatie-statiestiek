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