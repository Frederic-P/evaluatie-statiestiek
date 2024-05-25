"""
Utility to load a uniform style in multiple notebooks
"""

import matplotlib.pyplot as plt

def initialize_custom_style():
    """Loads a custom style for the entire notebook, 
    all graphs in that notebook will have the same style"""
    #remove top spine
    plt.rcParams['axes.spines.top'] = False
    #remove right spine   
    plt.rcParams['axes.spines.right'] = False
    #increase figure size to xy
    plt.rcParams['figure.figsize'] = [18, 6]
    #increase label sizes on axes
    plt.rcParams['axes.labelsize'] = 20
    #increase tick sizes
    plt.rcParams['xtick.labelsize'] = 15        
    plt.rcParams['ytick.labelsize'] = 15
    #bigger title
    plt.rcParams['axes.titlesize'] = 24         
    #remove the grid of a graph
    plt.rcParams['axes.grid'] = False           