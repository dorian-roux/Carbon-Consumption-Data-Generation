######################################
#   Carbon Impact - Data Generator   #
######################################

### Libraries
import numpy as np
import random
import pandas as pd
import seaborn as sns
import datetime
import matplotlib.pyplot as plt
import os 

#Function to append the value to the corresponding dictionnary key
def append_dict(data_dict, lst_key, lst_value):
    for key, val in zip(lst_key, lst_value):
        data_dict[key].append(val)
    return data_dict

#Function that generate values corresponding to some conditions
def generate_time_data(current_daytime, weekdays):
    year = current_daytime.year
    month = current_daytime.month
    day = current_daytime.day
    weekday = weekdays[current_daytime.weekday()]
    time_hm = current_daytime.time()
    date = datetime.datetime(year, month, day)
    return date, year, month, day, weekday, time_hm



#Read CSV file
sample_apps = pd.read_csv("Data/apps.csv", delimiter=';')
s = sample_apps.sample(10).reset_index()
s[['Application', 'Actions', 'Carbon_Impact']]

