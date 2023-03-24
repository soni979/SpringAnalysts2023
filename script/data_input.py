""" 

Repository of input functions to retrieve data

Contact: Ricky Renner, Joe Ratterman, Andy Lundberg
Date: 2/3/2023
Status: In progress

"""

## Library Imports
import pandas as pd
import yaml

import keyring
import cx_Oracle
import os
from datetime import date
import time

#from sharepoint_client import SharepointClient
#from office365.runtime.auth.user_credential import UserCredential

import pyodbc

import data_output as do_script

## Functions
def sql_oracle(sql, user, userpass, host, port, sid):
    """ Connect to an Oracle Database using stored credentials
    Date: Many Moons Ago
    Args:
        sql -- sql script
        user -- db username
        passw -- db password
        host -- db host name
        port -- db port
        sid -- db sid
    Return:
        Table returned from SQL script
    """

    start = time.time()
    full_sql = sql
    dsn = cx_Oracle.makedsn(host, port, sid)
    orcl = cx_Oracle.connect(user=user, password=userpass, dsn=dsn)
    df_ora = pd.read_sql(full_sql, con=orcl)
    print("--- %s seconds to load %s ---" % (round(time.time() - start, 3), sql))
    return df_ora

def oracle_data_import():
    """ Import data from Oracle using config file credentials and keyring password. Initially setup to export to pickle files in exports folder.
    Date: 11/11/2022
    Args:
        oracle-connection[domain]
        oracle-connection[user]
        oracle-connection[host]
        oracle-connection[port]
        oracle-connection[sid]
        oracle-connection[export-directory] - directory containing sql files
    """
    # Retrieve credentials from config file
    with open("config.yaml") as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
        domain = config["oracle-connection"]["domain"]
        user = config["oracle-connection"]["user"]
        db_host = config["oracle-connection"]["host"]
        db_port = config["oracle-connection"]["port"]
        db_sid = config["oracle-connection"]["sid"]
        directory = config["export-directory"]

    userpass = keyring.get_password(domain, user)

    ## For each (daily loaded) file run following:
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # Check that current export does not exist and if it does current_date is not today
        # If true run the following
        dt = sql_oracle(f, user, userpass, db_host, db_port, db_sid)

        # Add in current_date column
        dt["current_date"] = date.today()

        # Export to file
        do_script.file_data_export(dt,
            os.path.join("exports/", filename.replace(".sql", ".pkl"))
        )

def excel_data_import(manual_data):
    """ Import data from manual excel file into dataframe as tabname and then export into exports folder
    Date: 11/11/2022
    Args:
        manual-tables - filepath to excel spreadsheet
    """

    excel_sheet = pd.ExcelFile(manual_data)

    # Loop through each sheet of the manual excel file and create tables using the tab names
    for sheet in excel_sheet.sheet_names:
        # Load data from individual sheet
        dt = excel_sheet.parse(sheet)

        # Add in current_date column
        dt["current_date"] = date.today()

        # Export to file
        do_script.file_data_export(dt, os.path.join("exports/", sheet + ".pkl"))

def sharepoint_data_import(name, username, url, dir, file):
    """ Connect to Sharepoint using username, url, directory path, and filename. Initially setup to export to pickle files in exports folder.
    Date: 12/15/2022
    Args:
        name - desired pickle file name
        username
        url - Sharepoint URL
        dir - directory path to where desired file sits in sharepoint
        file - filename with extension
    """
    password = 'password'

    user_credentials = UserCredential(user_name=username, password=password)
    sharepoint_client = SharepointClient(
        sharepoint_url=url,
        default_download_directory='./',
        user_credentials=user_credentials
    )

    sharepoint_directory = dir
    sharepoint_file_name = file
    
    dt = sharepoint_client.get_file_names_in_sharepoint_folder(sharepoint_directory=sharepoint_directory)
    
    # Export to file
    do_script.file_data_export(dt, os.path.join("exports/", name + ".pkl"))

def odbc_data_import(name: str, query: str, connection_str: str, chunksize=0):
    """ Convert query to a list of pandas data frames. List size depends on chunk size and records in query result. Initially setup to export to pickle files in exports folder.
    Date: 4/16/2022
    Args:
        name - desired pickle file name
        query 
        connection_str
        chunksize - optional
    return: 
        sql_queries - list of pandas data frames
    """
    conn = pyodbc.connect(connection_str)

    if chunksize > 0:
        sql_queries = pd.read_sql_query(sql=query, con=conn, chunksize=chunksize)
    else:
        sql_queries = [pd.read_sql_query(sql=query, con=conn)]

    # Export to file
    do_script.file_data_export(sql_queries, os.path.join("exports/", name + ".pkl"))
    
    return sql_queries