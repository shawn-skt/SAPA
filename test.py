from base64 import encode
import pandas as pd

df = pd.read_csv('test.csv')
df = df[df['area']=='计算机网络']
df.to_csv('network.csv')
print(df)

# print([None]*10)