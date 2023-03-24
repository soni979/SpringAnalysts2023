# Script Annotation
This script was automatically generated using the 'create-readme.py' script. If any fields are incorrect please make sure the comment patterns below are used in the script.

Script files are commented as follows:

    """file-summary-text
        Contact: contact-text
        Date: date-text
        Status: status-text
        """

Functions in script are commented as follows:

    """function-summary-text
        Date: date-text
        Args:
            arg-bullets
        Return:
            return-bullets
        """

## test_script.py
**Date**: 10/01/2022

**Status:** Completed

Test Script, shows how to read config YAML file

**Library**:
* yaml
* logging

### read_config

Summary: Example of how to read in YAML file contents and use them

Date: 2/3/2023

Arguments: 
* config_file - path to config YAML file

## data_input.py
**Date**: 2/3/2023

**Status:** In progress

Repository of input functions to retrieve data

**Library**:
* pandas
* yaml
* keyring
* cx_Oracle
* os
* date
* time
* SharepointClient
* UserCredential
* pyodbc
* data_output

### sql_oracle

Summary: Connect to an Oracle Database using stored credentials

Date: Many Moons Ago

Arguments: 
* sql -- sql script
* user -- db username
* passw -- db password
* host -- db host name
* port -- db port
* sid -- db sid

Return
* Table returned from SQL script

### oracle_data_import

Summary: Import data from Oracle using config file credentials and keyring password. Initially setup to export to pickle files in exports folder.

Date: 11/11/2022

Arguments: 
* oracle-connection[domain]
* oracle-connection[user]
* oracle-connection[host]
* oracle-connection[port]
* oracle-connection[sid]
* oracle-connection[export-directory] - directory containing sql files

### excel_data_import

Summary: Import data from manual excel file into dataframe as tabname and then export into exports folder

Date: 11/11/2022

Arguments: 
* manual-tables - filepath to excel spreadsheet

### sharepoint_data_import

Summary: Connect to Sharepoint using username, url, directory path, and filename. Initially setup to export to pickle files in exports folder.

Date: 12/15/2022

Arguments: 
* name - desired pickle file name
* username
* url - Sharepoint URL
* dir - directory path to where desired file sits in sharepoint
* file - filename with extension

### odbc_data_import

Summary: Convert query to a list of pandas data frames. List size depends on chunk size and records in query result. Initially setup to export to pickle files in exports folder.

Date: 4/16/2022

Arguments: 
* name - desired pickle file name
* query
* connection_str
* chunksize - optional

Return
* sql_queries - list of pandas data frames

## data_output.py
**Date**: 2/6/2023

**Status:** In progress

Repository of output functions to write data

**Library**:
* pandas

### file_data_export

Summary: Export pandas dataframe into a pickle or csv file. Will overwrite files. Defaults to df-export.pkl in script folder.

Date: 2/6/2023

Arguments: 
* df - dataframe to write out
* output - optional, path to where to write out to. Needs extension (pkl, csv).
