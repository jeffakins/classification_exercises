# Data Acquisition Exercises

import env
import pandas as pd
import numpy as np
import os

#-----------------------------------------------------------------------------------

# Connection information for the mySQL Server

def get_connection(db, user=env.username, host=env.hostname, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

#-----------------------------------------------------------------------------------

# Titanic Data Set from CODEUP's mySQL Server 
def get_titanic_data():
    sql = 'SELECT * FROM passengers;'
    db = 'titanic_db'
    df = pd.read_sql(sql, get_connection(db))
    return df

 # Iris Dataset   
#def get_iris_data():
#    return 
