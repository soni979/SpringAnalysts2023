""" 

Test Script, shows how to read config YAML file

Contact: 
Date: 10/01/2022
Status: Completed

"""

## Library Imports
import yaml
import logging

## Functions
def read_config(config_file):
  """
  Example of how to read in YAML file contents and use them
  Date: 2/3/2023
  Args:
    config_file - path to config YAML file"""
  
  example_parameter = ""

  try:
     with open(config_file) as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
        
        # Read in each parameter; first try to find, if not present catch error and exit
        try:
          example_parameter = config["example-parameter"]
        except KeyError:
          logging.error("No example-parameter found in config")
          exit()
          
        # Read in list parameters (similar to normal)
        try:
          example_parameter = config["example-list"]["item-1"]
        except KeyError:
          logging.error("No example-list item-1 found in config")
          exit()
        
  except FileNotFoundError:
    logging.error('Config file not found') 
