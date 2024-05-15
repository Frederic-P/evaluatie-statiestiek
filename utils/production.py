import os
import pandas as pd

def load_json_datafiles(rootdir, colname = 'facility'):
    """Load the JSON data for the production dataset.
    Pass the directory where data for each factory is
    organized per folder. Data will be returned in a 
    single dataframe with the name of the factory as 
    an extra column. The name of the column can be 
    passed as an optional argument."""
    for r,d,f in os.walk(rootdir): 
        print(d)
    return d
if __name__ == 'main':
    print('hello') 
    dir = r"C:\Practical Business Python\projecten\derde project\evaluatie statiestiek\data\rawdata\full\data_productie\daily_production"
    print(dir)
    load_json_datafiles(dir)