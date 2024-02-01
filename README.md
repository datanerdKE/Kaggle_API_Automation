# Kaggle API Automation

This repository contains a Python script for extracting and loading data related to data science job postings from a zip file into a MySQL database.
## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Search for the Dataset](#i-search-for-the-dataset)
  - [Download the Dataset](#ii-download-the-dataset)
- [Database Connection](#database-connection)
- [Data Cleaning](#data-cleaning)
- [Export to Database](#5-export-to-database)
  - [Before running the Python script](#6-before-running-the-python-script)
- [License](#license)

## Prerequisites

Make sure you have the following installed:

- Python
- MySQL
- Necessary Python packages (you can install them using `pip install -r requirements.txt`)

## 1. Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

## 2. Usage

### i. Search for the Dataset

To search for the dataset on Kaggle, use the following command:

```bash
kaggle datasets list -s 'Data Analyst Job Postings [Pay, Skills, Benefits]'
```

### ii. Download the Dataset

To download the dataset using the Kaggle API, run:

```bash
kaggle datasets download -d 'lukebarousse/data-analyst-job-postings-google-search'
```

## 3. Database Connection

Uncomment and update the following lines in the script to connect to your MySQL database:

```python
  db = mysql.connector.connect(user='your-username', database='your-database', password='your-password')
  cursor = db.cursor()
  cursor.execute('create database gsearch_jobs')
  cursor.close()
  db.close()
```
Update the MySQL engine connection string:
```python
mysql_engine = create_engine('mysql://your-username:your-password@localhost:3306/gsearch_jobs')
```

## 4. Data Cleaning

The script performs basic data cleaning, dropping unnecessary columns from the dataset.

```python
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
```

## 5. Export to Database

The cleaned dataset is exported to the local MySQL database.

Create database connection to Local MySQL database using SQLAlchemy:

```python
dataframe.to_sql('data_science_jobs',mysql_engine,index=False,if_exists='replace')
```

### 6. Before running the Python script, make sure to update the necessary configuration settings in `export_jobs.py`

- Open the `export_jobs.py` script.
- Locate the database connection details.
- Update the values for 'your-username', 'your-database', and 'your-password' based on your MySQL configuration.

Then, run the script to extract, load, and clean the data.
```bash
python export_jobs.py
```

## License

This project is licensed under the MIT License 
