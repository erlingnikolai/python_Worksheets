import pandas as pd
from scipy import stats, math

url = "http://wps.aw.com/wps/media/objects/14/15269/projects/ch6_iq/brain.txt"

df = pd.read_table(url, sep ="\t")
female = df[df["Gender"] == "Female"]
a = df.loc[:, "Height"]
retard = []
for x in a:
    if math.isnan(x):
        print(x)
    else:
        retard.append(x)
#print(a.describe())

tihi =stats.ttest_1samp(a =retard, popmean =163)
print(tihi)




















