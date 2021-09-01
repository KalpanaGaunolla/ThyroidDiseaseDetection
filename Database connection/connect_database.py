

#Connecting to MongoDB database from local system
#Import necessary libraries
#Add logs to the code
from numpy import lookfor, recarray
import pymongo
from pymongo import MongoClient
import pandas as pd
import json
import logging

#Configuring the logging system
logging.basicConfig(filename='test.log',level=logging.DEBUG,format='%(levelname)s:%(asctime)s:%(message)s')

Client=MongoClient('localhost',27017)

    
##Inserting the preprocessed data into Database

def InsertData(path):
    
    DB=Client['Data']
    collection=DB['Thyroid']
    df=pd.read_csv(path)
    data=df.to_dict('records')
    collection.insert_many(data,ordered=False)
    logging.debug('All the data has been exported to MongoDB server')

#Fetchig the database into python from MongoDB

def getData(collection):

    records=collection.find()
    import_data=pd.DataFrame(list(records))
    logging.debug(import_data))


if __name__=='__main__':
    mongodb=InsertData(path='Thyroid_Data.csv')
    #data=getData(collection=collection)








