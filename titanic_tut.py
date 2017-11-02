import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# matplotlib inline

data_train = pd.read_csv('train.csv')
data_test =  pd.read_csv('test.csv')
# print (data_train.head())

o = data_train.sample(3)
print (o)
