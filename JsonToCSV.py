import json
import pandas as pd

# Name test file
filename = 'test4'

#load data from test file
with open (filename + '.json') as f:
    data = json.load(f)

#load data frame with json data and remove duplicates
df = pd.json_normalize(data, record_path=['signals'],meta=['distance','trail'])
df = df.drop_duplicates()

#print data and save in a csv format
pd.set_option("max_rows", None)
print(df.groupby(['mac','trail','dataRate']).agg({'rssi': ['median','count','std']}))
df.to_csv( filename + '.csv')

