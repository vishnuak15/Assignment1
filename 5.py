import csv
import pandas as pd 
df = pd.read_csv("myfile.csv")
df1=df.stud_nam
df2 = pd.DataFrame({'totl_mrks':df.sum(axis=1)})
df3= pd.DataFrame({'avg_mrks':df.mean(axis=1)})
frames = [df1, df2, df3]
result = pd.concat(frames, axis=1)
result.to_csv('city.csv')