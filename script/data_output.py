""" 

Repository of output functions to write data

Contact: Andrea Gergel
Date: 2/6/2023
Status: In progress

"""
## Library Imports
import pandas as pd

## Functions
def file_data_export(df, output = "df-export.pkl"):
    """ Export pandas dataframe into a pickle or csv file. Will overwrite files. Defaults to df-export.pkl in script folder.
    Date: 2/6/2023
    Args:
        df - dataframe to write out
        output - optional, path to where to write out to. Needs extension (pkl, csv). 
    """
    if output.lower().endswith('.pkl'):
        df.to_pickle(output)
    elif output.lower().endswith('.csv'):
        df.to_csv(output)


