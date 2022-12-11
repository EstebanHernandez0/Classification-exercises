import pandas as pd
import numpy as np
import os
from env import get_connection

def new_titanic_data():

    sql_query = 'SELECT * FROM passengers'
    
    # connects to the database from codeup
    df = pd.read_sql(sql_query, get_connection('titanic_db'))
    
    return df

def get_titanic_data():

    if os.path.isfile('titanic_df.csv'):
        
        # If csv file exists, read in data from csv file
        df = pd.read_csv('titanic_df.csv', index_col=0)
        
    else:
        # re runs the original titanic data
        df = new_titanic_data()
        
        # turns it into a csv file
        df.to_csv('titanic_df.csv')
        
    return df

def new_iris_data():

    sql_query = """
                SELECT 
                    species_id,
                    species_name,
                    sepal_length,
                    sepal_width,
                    petal_length,
                    petal_width
                    measurment_id
                FROM measurements
                JOIN species USING(species_id)
                """
    
    # Read in DataFrame from Codeup db.
    df = pd.read_sql(sql_query, get_connection('iris_db'))
    
    return df

def get_iris_data():

    if os.path.isfile('iris_df.csv'):
        
        df = pd.read_csv('iris_df.csv', index_col=0)
        
    else:
        
        # re run original iris data
        df = new_iris_data()
        
        df.to_csv('iris_df.csv')
        
    return df

def new_telco_data():
    
    sql_query = """
                select * from customers
                join contract_types using (contract_type_id)
                join internet_service_types using (internet_service_type_id)
                join payment_types using (payment_type_id)
                """
    
    # Read in DataFrame from Codeup db.
    df = pd.read_sql(sql_query, get_connection('telco_churn'))
    
    return df

def get_telco_data():
    
    if os.path.isfile('telco.csv'):
        
        # If csv file exists read in data from csv file.
        df = pd.read_csv('telco.csv', index_col=0)
        
    else:
        
        df = new_telco_data()

        df.to_csv('telco.csv')
        
    return df