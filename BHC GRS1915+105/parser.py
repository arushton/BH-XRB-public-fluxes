import pandas as pd
import json

# Read the .dat file
df = pd.read_csv('grs1915_rt-15GHz.dat', sep="\s+", names=['MJD', 'Flux'])

# Convert the DataFrame to a list of dictionaries
data_dict = df.to_dict('records')

# Write out the .json file
with open('grs1915_rt-15GHz.json', 'w') as f:
    json.dump(data_dict, f)
