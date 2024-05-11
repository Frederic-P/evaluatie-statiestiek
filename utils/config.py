import json
import os
#utilities to read configuration: 

def get_root_dir():
    """function returns the absolute path of the root directory. 
    the root directory is the directory holding the utils, data
    and notbeooks folder: """
    utils_dir = os.path.abspath(os.path.dirname(__file__))
    root_dir = os.path.abspath(os.path.join(utils_dir, os.pardir))
    #check that root_dir contains the notebook and utils directory: 
    root_dir_contents = os.listdir(root_dir)
    if ('config' in root_dir_contents and 
        'notebooks' in root_dir_contents):
        return root_dir
    else:
        raise Exception("Root directory not found!")



def read(dir_to_config): 
    """reads a json config file and returns it as a kv dictionary"""
    with open(dir_to_config) as settings_file:
        settings = json.load(settings_file)
        return settings
    
