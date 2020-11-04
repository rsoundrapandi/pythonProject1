
import pandas as pd


def header(msg):

    filename='Testfile2.csv'
    df2=pd.read_csv(filename)
    print(df2)
    print("test")


header('msg')


import os

print(os.getcwd())


import random

print(random.randint(1,1000))