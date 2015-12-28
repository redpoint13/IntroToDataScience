import itertools
import csv
import pandas as pd

df = pd.read_csv('turnstile_data_master_with_weather.csv')
f_out = open('header_combiniations.csv', 'w')

df = df.drop(df.columns[[0]], axis=1)
df = df.drop('EXITSn_hourly', 1)
headers = list(df)
print headers
"""
for L in range(1, len(headers)+1):
    print L

  for subset in itertools.combinations(headers, L):
    print(subset)
    #f_out.write(str(subset) + '\n')
"""

f_out.close()
