import pandas as pd

df1 = pd.read_csv('athlete_events.csv')
df2 = pd.read_csv('noc_regions.csv')

df = df1.merge(df2, on = 'NOC', how = 'left')

def preprocess():
    global df1, df2
    df1 = df1[(df1['Season'] == 'Summer')]
    df = df1.merge(df2, on='NOC', how='left')
    df.drop_duplicates(inplace=True)
    df = pd.concat([df1, pd.get_dummies(df1['Medal'])], axis=1)
    return df
