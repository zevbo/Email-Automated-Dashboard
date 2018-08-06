import csv
import sys
import pandas as pd

df = pd.read_csv("export.csv", dtype={"Name" : str, "Subject" : str, "Sent On" : str, "Sent" : str, "Unique Opens" : str, "Unique Clicks" : str, "Opt Outs" : str})

CUTOFF = 500
year = sys.argv[1]
month = sys.argv[2]
date = year + "-" + month

def makeDashboardRow(data):
   return [data["Name"],data["Subject"],data["Sent On"],data["Sent"],1,data["Unique Opens"],data["Unique Clicks"],"","","",data["Opt Outs"],""]

with open('dashboard.csv', 'ab') as f:                       
    writer = csv.writer(f)

    for index, row in df.iterrows():
        if int(row["Sent"]) > CUTOFF and row["Sent On"][:len(date)] == date:
            writer.writerow(makeDashboardRow(row))
            