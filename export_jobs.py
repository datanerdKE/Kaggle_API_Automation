# Import Packages
import zipfile  
import os             
import pandas as pd  
pd.set_option('display.max_columns',100)      
from sqlalchemy import create_engine
import mysql.connector

# DataBase Connection

# db = mysql.connector.connect(user='export',database='export',password='export')
# cursor = db.cursor()

# cursor.execute('create database gsearch_jobs')

# cursor.close()
# db.close()

mysql_engine = create_engine('mysql://export:export@localhost:3306/gsearch_jobs')

# file_name = 'data-analyst-job-postings-google-search.zip'

# Unzip and Load Data
data = 'data'
with zipfile.ZipFile('data-analyst-job-postings-google-search.zip', 'r') as zip_ref:
    zip_ref.extractall(data)
os.remove('data-analyst-job-postings-google-search.zip')

for index in os.listdir(data):
    dataframe = pd.read_csv(os.path.join(data,index))
    os.remove(os.path.join(data,index))
    
# Basic Data Cleaning
dataframe.drop(['Unnamed: 0','commute_time', 'salary_pay', 'salary_rate','job_id','thumbnail','index',
    'salary_avg', 'salary_min', 'salary_max', 'salary_hourly','search_term','search_location',
    'salary_yearly', 'salary_standardized',],axis=1,inplace=True)

# Export to Local Database
dataframe.to_sql('data_science_jobs',mysql_engine,index=False,if_exists='replace')
print(f"Shape of the Dataset : {dataframe.shape}")