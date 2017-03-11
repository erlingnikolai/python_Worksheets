import numpy as np
import scipy.stats as stats
import pandas as pd

url = "https://www.national-lottery.co.uk/results/lotto/draw-history/csv"


def part_one():
    intArray = np.random.randint(10, high=100, size=10)
    print("numbers = ", intArray)
    print("median = ", np.median(intArray))
    print("mean = ", np.mean(intArray))
    print("variance = ", np.var(intArray))
    print("standard deviation = ", np.std(intArray))
    print("mod = ", stats.mode(intArray))


def part_two():
    data_brain = pd.read_csv(url, na_values=".")
    all_bonus_balls = data_brain.loc[:, "Bonus Ball"]
    print("mean = ", np.mean(all_bonus_balls))
    print("variance = ", np.var(all_bonus_balls))
    print("standard deviation = ", np.std(all_bonus_balls))
    print(all_bonus_balls.describe())


part_two()
print(url)
