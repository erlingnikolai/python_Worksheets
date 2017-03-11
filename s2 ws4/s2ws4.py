import pandas as pd
from scipy import stats, math

url = "http://wps.aw.com/wps/media/objects/14/15269/projects/ch6_iq/brain.txt"

df = pd.read_table(url, sep ="\t")
female = df[df["Gender"] == "Female"]
male = df[df["Gender"] == "Male"]
a = female.loc[:, "Height"]
b = male.loc[:, "Height"]


def find_info(temp):
    something = []
    for x in temp:
        if not math.isnan(x):
            something.append(x)
    return something


test_male = stats.ttest_1samp(a=find_info(b), popmean=170)
test_female = stats.ttest_1samp(a=find_info(a), popmean=163)
test_compare = stats.ttest_ind(a=find_info(a), b=find_info(b))

print(test_male)
print(test_female)
print(test_compare)