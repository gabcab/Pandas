import pandas as pd

'''
 read_excel()
 read_csv()
 read_sql_table()
 read_json()
'''
oo = pd.read_csv("./data/olympics.csv", skiprows=4)
print(oo.head())
