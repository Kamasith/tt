# import packages
import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()
plt.rcParams['axes.unicode_minus']=False


# show the title
st.title('Titanic App by Guanghao Li')

# read csv and show the dataframe
t=pd.read_csv('train.csv')

# create a figure with three subplots, size should be (15, 5)
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below
fig, ax = plt.subplots(1, 3, figsize=(15,5))


t[t['Pclass'] == 1].Fare.plot.box(ax = ax[0])
t[t['Pclass'] == 2].Fare.plot.box(ax = ax[1])
t[t['Pclass'] == 3].Fare.plot.box(ax = ax[2])
ax[0].set_xlabel('Pclass = 1')
ax[1].set_xlabel('Pclass = 2')
ax[2].set_xlabel('Pclass = 3')
ax[0].set_ylabel('Fare')
