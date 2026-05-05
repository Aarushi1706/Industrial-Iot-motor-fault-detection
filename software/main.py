import pandas as pd
import numpy as np
import os
from scipy.stats import kurtosis
print("Current folder:", os.getcwd())
print("Files in this folder:", os.listdir())

# load your dataset
df = pd.read_csv("resistor_data.csv") 

window_size = 20
step = 20   # use 10 for overlapping

features = []

for i in range(0, len(df) - window_size, step):
    window = df.iloc[i:i+window_size]
    
    # Current features
    curr = window['current']
    mean_curr = curr.mean()
    rms_curr = np.sqrt(np.mean(curr**2))
    std_curr = curr.std()
    
    # Temperature features
    temp = window['temperature']
    mean_temp = temp.mean()
    temp_rate = (temp.iloc[-1] - temp.iloc[0]) / window_size
    
    # Vibration features
    vib = window['vib']
    rms_vib = np.sqrt(np.mean(vib**2))
    std_vib = vib.std()
    peak_vib = vib.max()
    crest = peak_vib / rms_vib
    kurt = kurtosis(vib)
    
    features.append([
        mean_curr, rms_curr, std_curr,
        mean_temp, temp_rate,
        rms_vib, std_vib, peak_vib, crest, kurt
    ])

# convert to dataframe
feature_df = pd.DataFrame(features, columns=[
    'mean_curr','rms_curr','std_curr',
    'mean_temp','temp_rate',
    'rms_vib','std_vib','peak_vib','crest','kurtosis'
])

print(feature_df.head())
feature_df['label'] = 'highCurrent'  
feature_df.to_csv("highCurrent_features.csv", index=False)