from dotenv import load_dotenv
import pandas as pd 
import os
load_dotenv()



def get_executor(credentials):
    try:
        executor = eval(os.getenv("executor"))
        properties = executor[credentials]
        return properties
    except Exception as e:
        print(f'error en get_executor() in PropertieController.py: {e}')


def get_retailers():
    try:
        retailers = os.getenv('retailers')
        return retailers
    except Exception as e:
        print(f'error en get_retailers() in PropertieController.py: {e}')


def get_countries():
    try:
        countries = os.getenv('countries')
        return countries
    except Exception as e:
        print(f'error en get_countries() in PropertieController.py: {e}')

countries = eval(get_countries())
retailers = eval(get_retailers())

def df_get():
    #dataframe = GetDataFrame('product_homologated','psql_read').get_dataframe # crawling > retail_information -- homologados > product_homologated
    #dataframe.to_csv('product.csv', index=False)
    dataframe = pd.read_csv("product.csv")
    dataframe = dataframe[dataframe['PAIS'].isin(countries)] # country - PAIS
    dataframe = dataframe[dataframe['RETAILER'].isin(retailers)] # retail - RETAILER
    return dataframe

#for i, df in dataframe.iterrows():
    #print (df['URL'])
