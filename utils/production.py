import os
import pandas as pd
import json
import numpy as np
from scipy.stats import *

def get_failure_rate(prepdata):
    """takes a single argument prepdata which is the pandas dataframe
    without 0-production days for planned downtime. Returns a dict with 
    the location code as key and the percentual amount of 0-production
    days per location"""
    no_production_chance = {}
    for facility, group in prepdata.groupby('facility'): 
        ##you need to extract the ratio of days with UNPLANNED zero production over the total days of planned production
        no_production_chance[facility] = group.query('production == 0').shape[0]/group.shape[0]
    return no_production_chance

def generate_prediction_normfit(productiondata):
    """takes productiondata as an argument which is the pandas dataframe
    holding all datapoints for all facilities where actual production took 
    place (filtered out ALL 0-output days)
    
    returns the result of norm.fit for each productionfacility. """
    dictreturn = {} 
    for facility, group in productiondata.groupby('facility'): 
        dictreturn[facility] = norm.fit(group['production'])
    return dictreturn

def simulate(n_days, failurerate, predictions): 
    """Takes three argumens: prediction horizon. 
    n_days (int) = length of prediction horizon. 
    failurerate (float) = days in percent without planned maintenance and 0 production
    predictions

    ALL argumens passed should be specific data for the given facility. SO do not pass
    the full dicts of all failurerates and mean/stdevs

    """
    production = []
    delta = 10 ** -6
    for _ in range(n_days): 
        #get the chance of total failure at facility:
        chance_of_catastrophe = np.random.rand() 
        if failurerate - chance_of_catastrophe > delta:
            #total fuck up :)
            production.append(0)
        else:
            mean, stdev = predictions
            result_of_scipy = norm.rvs(loc=mean, scale=stdev, size=1)[0]
            production.append(result_of_scipy)
    return production

def merged_production(*all_production_lists): 
    """Takes as argument a single list of multiple sublists. Each sublist
    is the projected production for a single factory. The function returns
    the expected production across all locations. When it is given the extended
    dictionary produced by get_prod_estimate_per_facility it'll reduce the values
    to a list """
    max_length = max(map(len, all_production_lists))
    sum_over_list = [sum(prod) for prod in zip(*[lst + [0]*(max_length - len(lst)) for lst in all_production_lists])]
    return sum_over_list

def get_prod_estimate_per_facility(ndays, failratesdict, predictionratesdict, facility_locations, reduced = True): 
    """required ndays argument = int: how many days do you want
    to include in the projection. 
    reduced = optional bool = (default = true): Set to false to 
    return a dict with precise production per facility. If reduece
    is true, it will return a list without keys to indicate each 
    location's output. 
    failratesdict is a dictionary with the percentual failure rate per 
    location
    """
    facilities_production = {}
    for loc in facility_locations:
        failrate = failratesdict[loc]
        predictionrate = predictionratesdict[loc]
        facilities_production[loc] = simulate(ndays, failrate, predictionrate)
    if reduced:
        return list(facilities_production.values())
    else:
        return facilities_production
       


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
