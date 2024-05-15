import os
import pandas as pd
import json

def load_json_datafiles(rootdir, colname = 'facility'):
    """Load the JSON data for the production dataset.
    Pass the directory where data for each factory is
    organized per folder. Data will be returned in a 
    single dataframe with the name of the factory as 
    an extra column. The name of the column can be 
    passed as an optional argument."""
    dataset = []
    for location in os.listdir(rootdir):
        #print(location)
        locationdir = os.path.join(rootdir, location)
        for file in os.listdir(locationdir):
            with open(os.path.join(locationdir, file)) as filecontent:
                filedata = json.load(filecontent)
                #keep track of where the datapoint comes from 
                #in case weird stuff happens.
                filedata['sourcefile'] = file
                filedata['facility'] = location
                dataset.append(filedata)
    return dataset
    # for r,d,f in os.walk(rootdir): 
    #     for location in d: 
    #         print(location)
    #         for file in os.path.join(rootdir,f:
    #             print(file)
    # #return d
