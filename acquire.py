# Data Acquisition Exercises

#---------------------------Imports---------------------------------------------------

import env
import pandas as pd
import numpy as np
import os

#---------------------------Connection Info--------------------------------------------

# Connection information for the mySQL Server

def get_connection(db, user=env.username, host=env.hostname, password=env.password):
    connection_info = f'mysql+pymysql://{user}:{password}@{host}/{db}'
    return connection_info

#---------------------------Data Base Functions----------------------------------------

# Function to retrieve the Titanic Data Set from CODEUP's mySQL Server 
def get_titanic_data():
    if os.path.isfile('titanic_df.csv'):
        df = pd.read_csv('titanic_df.csv', index_col=0) # If csv file exists read in data from csv file.
    else:
        sql = 'SELECT * FROM passengers;'               # SQL query
        db = 'titanic_db'                               # Database name
        df = pd.read_sql(sql, get_connection(db))       # Pandas DataFrame
        df.to_csv('titanic_df.csv')                     # Cache Data
    return df

# Function to retrieve the Iris Dataset   
def get_iris_data():
    if os.path.isfile('iris_df.csv'):
        df = pd.read_csv('iris_df.csv', index_col=0)    # If csv file exists read in data from csv file.
    else:
        sql = 'SELECT * FROM measurements JOIN species USING(species_id);'
        db = 'iris_db'
        df = pd.read_sql(sql, get_connection(db))       # Read fresh data from db into a DataFrame
        df.to_csv('iris_df.csv')                        # Cache data 
    return df

