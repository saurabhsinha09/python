import os
import time
import pandas as pd

if os.path.exists("temps_today.csv"):
    data = pd.read_csv("temps_today.csv")
    print(data.mean())
    print(data["st1"].mean())
else:
    print("file does not exist")