## Python packages - you may have to pip install sqlalchemy, sqlalchemy_utils, and psycopg2.
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import psycopg2
import pandas as pd

#In Python: Define your username and password used above. I've defined the database name (we're
#using a dataset on births, so I call it birth_db).
dbname = 'yammer_db'
username = 'davestanley'
pswd = 'coco'

## 'engine' is a connection to a database
## Here, we're using postgres, but sqlalchemy can connect to other things too.
engine = create_engine('postgresql://%s:%s@localhost/%s'%(username,pswd,dbname))
print('postgresql://%s:%s@localhost/%s'%(username,pswd,dbname))
print(engine.url)
# Replace localhost with IP address if accessing a remote server

## create a database (if it doesn't exist)
if not database_exists(engine.url):
    create_database(engine.url)
print(database_exists(engine.url))
print(engine.url)


# load a database from the included CSV
# edit the string below to account for where you saved the csv.
import os

csv_path = os.path.join('.','yammer_events.csv')
data = pd.read_csv(csv_path)
data.to_sql('yammer_events', engine, if_exists='replace')


csv_path = os.path.join('.','yammer_emails.csv')
data = pd.read_csv(csv_path)
data.to_sql('yammer_emails', engine, if_exists='replace')

csv_path = os.path.join('.','yammer_users.csv')
data = pd.read_csv(csv_path)
data.to_sql('yammer_users', engine, if_exists='replace')

csv_path = os.path.join('.','dimension_rollup_periods.csv')
data = pd.read_csv(csv_path)
data.to_sql('dimension_rollup_periods', engine, if_exists='replace')
