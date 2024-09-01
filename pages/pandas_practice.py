import pandas as pd
import streamlit as st
import numpy as np

st.title("Pandas Examples")

# A list of integers
x1 = pd.Series([1,2,3,4,5])
st.write("Series with integers: ", x1)

# A list of integers and floats
x2 = pd.Series([1,2,3,4,5,3.5])
st.write("Series with integers and float: ", x2)

# A list of integers and a string
x3 = pd.Series([1,2,3,4,5,'a'])
st.write("Series with integers and a string: ", x3)

# A list of Strings
x4 = pd.Series(['apple', 'papayas', 'bananas', 'orange'])
st.write("Series with strings: ", x4)

# Creating a DataFrame from a Numpy Array
n1 = np.array([[1,2,3], [4,5,6], [7,8,9]])
df1 = pd.DataFrame(n1)
st.write("DataFrame from numpy: ", df1)

# Creating a series from list
l2 = [1,2,3,4,5]
s2 = pd.Series(l2, name='A')
st.write("Series from list with column name: ", s2)

n2 = np.array([[1,2,3], [4,5,6], [7,8,9]])
df2 = pd.DataFrame(n2, columns=['A', 'B', 'C'])
st.write("DataFrame from numpy array with column names: ", df2)

# Creating a DataFrame with column and row names
df3 = pd.DataFrame(n2, columns=['A', 'B', 'C'], index=['R1', 'R2', 'R3'])
st.write("DataFrame with column and row names: ", df3)

# Row names (i.e., the index) in a DataFrame can be renamed by .index
df4 = df3.copy()
df4.index = ['John', 'Mary', 'Somchai']
st.write("DataFrame with row names changed: ", df4)

# dataframe from dict
d = {'A': [1,2,3], 'B': [4,5,6], 'C': [7,8,9]}
df6 = pd.DataFrame(d, index=['John', 'Somchai', 'Sally'])
st.write("DataFrame from dict: ", df6)

# read csv file from web
df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv')
st.write("Head: \n", df.head())
st.write("Tail: \n", df.tail())

st.write("Select single column: \n")

st.write("First way df['MolLogP'] :\n", df['MolLogP'])

st.write("Second way df.MolLogP: \n", df.MolLogP)

st.write("Third way df.loc[:, 'MolLogP']: \n", df.loc[:, 'MolLogP'])

st.write("Fourth way df.iloc[:, 0]: \n", df.iloc[:, 0])

st.write("Selecting multiple columns: \n")

st.write("df[['MolLogP','MolWt']]: \n", df[['MolLogP','MolWt']])

st.write(df.describe())