from lib2to3.pgen2.pgen import DFAState
import pandas as pd

def handle_dict(data, key):
    try:
        return data[key]
    except:
        return None

origin_data = pd.read_json('res.json')

df = pd.DataFrame()

df = origin_data[['title', 'keywords', 'pubAbstract', 'venue', 'year']]
df['venue'].dropna(inplace=True)
df['type'] = df['venue'].apply(lambda x: handle_dict(x, 't'))
df['raw'] = df['venue'].apply(lambda x: handle_dict(x, 'raw'))
del df['venue']
df.to_csv('res.csv', index=False)
print(df.head())