# get the script path
import os
script_dir = os.path.dirname(os.path.abspath(__file__))

#import csv file
import pandas as pd
data=pd.read_csv(os.path.join(script_dir, 'age_counts.csv'))

#covert to json
data.to_json(os.path.join(script_dir, 'age_counts.json'), orient='records')

#import cenus data
census_data=pd.read_csv(os.path.join(script_dir, 'census.csv'))
#covert to json
census_data.to_json(os.path.join(script_dir, 'census.json'), orient='records')