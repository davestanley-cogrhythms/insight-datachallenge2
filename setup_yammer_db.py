## Python packages
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import psycopg2
import pandas as pd

#Define username and db name
dbname = 'yammer_db'
username = 'davestanley'
pswd = 'coco'

# Connect to postgres database. sqlalchemy can connect to other db's as well
engine = create_engine('postgresql://%s:%s@localhost/%s'%(username,pswd,dbname))
print('postgresql://%s:%s@localhost/%s'%(username,pswd,dbname))
print(engine.url)

## create db
if not database_exists(engine.url):
    create_database(engine.url)
print(database_exists(engine.url))
print(engine.url)


# load db from csv and send to SQL
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
