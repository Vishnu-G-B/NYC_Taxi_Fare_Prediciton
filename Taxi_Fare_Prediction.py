import pandas as pd
import matplotlib.pyplot as plt
import os


df_train = pd.read_csv("./train.csv/train.csv",nrows=1000000)
print(df_train.head())
print(df_train.info)