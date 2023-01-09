import pandas as pd
import numpy as np
import os
from env import get_connection
from sklearn.model_selection import train_test_split

def prep_iris(iris):
    
    iris = iris.drop(columns=['species_id'])
    iris.rename(columns={'species_name': 'species'}, inplace=True)
    species_df = pd.get_dummies(iris.species, drop_first=True)
    iris = pd.concat([iris, species_df], axis=1)
    return iris



def prep_titanic(titanic):
    titanic = titanic.drop(columns=['class', 'embarked', 'passenger_id','deck'])
    titanic = titanic.dropna()
    encoded_vars = pd.get_dummies(titanic[['embark_town', 'sex']], drop_first=True)
    titanic = pd.concat([titanic, encoded_vars], axis=1)
    return titanic




def prep_telco_data(df):

    # Drop null values stored as whitespace    
    df['total_charges'] = df['total_charges'].str.strip()
    df = df[df.total_charges != '']
    
    # Convert to correct datatype
    df['total_charges'] = df.total_charges.astype(float)
    
    # Convert binary categorical variables to numeric
    df['gender_encoded'] = df.gender.map({'Female': 1, 'Male': 0})
    df['partner_encoded'] = df.partner.map({'Yes': 1, 'No': 0})
    df['dependents_encoded'] = df.dependents.map({'Yes': 1, 'No': 0})
    df['phone_service_encoded'] = df.phone_service.map({'Yes': 1, 'No': 0})
    df['paperless_billing_encoded'] = df.paperless_billing.map({'Yes': 1, 'No': 0})
    df['churn_encoded'] = df.churn.map({'Yes': 1, 'No': 0})
    
    # Get dummies for non-binary categorical variables
    dummy_df = pd.get_dummies(df[['multiple_lines', \
                              'online_security', \
                              'online_backup', \
                              'device_protection', \
                              'tech_support', \
                              'streaming_tv', \
                              'streaming_movies', \
                              'contract_type', \
                              'internet_service_type', \
                              'payment_type']], dummy_na=False, \
                              drop_first=True)
    
    # Concatenate dummy dataframe to original 
    df = pd.concat([df, dummy_df], axis=1)
    
    # Drop duplicate columns
    df.drop(columns=['payment_type_id', 'internet_service_type_id', 'contract_type_id', 'customer_id'], inplace=True)
    
    return df
 

###################    
    
def split_data(df, target=''):
        train, test = train_test_split(df, 
                               train_size = 0.8,
                               random_state=1349,
                              stratify=df[target])
        train, val = train_test_split(train,
                             train_size = 0.7,
                             random_state=1349,
                             stratify=train[target])
        return train, val, test
    
    
    






