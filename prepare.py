def prep_iris(iris):
    
    iris = iris.drop(columns=['species_id'])
    iris.rename(columns={'species_name': 'species'}, inplace=True)
    species_encoded = pd.get_dummies(iris.species, drop_first=True)
    iris = pd.concat([iris, species_encoded], axis=1)
    return iris



def prep_titanic(titanic):
    titanic = titanic.drop(columns=['class', 
                                'embarked',
                                'passenger_id',
                                'deck',
                                'age'])
    tianic = titanic.dropna()
    encoded_vars = pd.get_dummies(titanic[['embark_town', 'sex']], drop_first=True)
    titanic = pd.concat([titanic, encoded_vars], axis=1)
    return titanic





def prep_telco(telco):
    telco['total_charges'] = (telco.total_charges + '0').astype('float')
    telco = telco.drop(columns=['internet_service_type_id', 'contract_type_id', 'payment_type_id'])
    telco['gender_encoded'] = telco.gender.map({'Female': 1, 'Male': 0})
    telco['partner_encoded'] = telco.partner.map({'Yes': 1, 'No': 0})
    telco['dependents_encoded'] = telco.dependents.map({'Yes': 1, 'No': 0})
    telco['phone_service_encoded'] = telco.phone_service.map({'Yes': 1, 'No': 0})
    telco['paperless_billing_encoded'] = telco.paperless_billing.map({'Yes': 1, 'No': 0})
    telco['churn_encoded'] = telco.churn.map({'Yes': 1, 'No': 0})
    dummy_df = pd.get_dummies(telco[['multiple_lines', \
                              'online_security', \
                              'online_backup', \
                              'device_protection', \
                              'tech_support', \
                              'streaming_tv', \
                              'streaming_movies', \
                              'contract_type', \
                              'internet_service_type', \
                              'payment_type'
                            ]],
                              drop_first=True)
    telco = pd.concat( [telco, dummy_df], axis=1 )
    
    return telco






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