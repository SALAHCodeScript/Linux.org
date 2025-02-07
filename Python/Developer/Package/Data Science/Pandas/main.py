#!python3.13
import pandas as pd

array_2d = [['tom', 31], ['salah', 20]]
df = pd.DataFrame(array_2d, columns=['name', 'age'])

print(df)
print(df.head(1))

print(df.columns)
print(df.index.tolist())
