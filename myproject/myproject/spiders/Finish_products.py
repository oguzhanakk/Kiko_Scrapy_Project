import sqlite3
import pandas as pd

conn = sqlite3.connect('kiko_milano.db')
cursor = conn.cursor()

cursor.execute("Select link from kiko_milano Where action = 'stockAlert'")
list = cursor.fetchall()
"""
print("Library table information...")
for i in list:
    print(i)
"""

#df = pd.Dataframe(list, columns = ["link"])
#print(df)

conn.commit()
conn.close()
