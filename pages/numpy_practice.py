import numpy as np
import streamlit as st

st.title("Numpy Examples")

# Creating 0-D
x1 = np.array(0)
st.write("Show 0-D numpy: ", x1)

# Creating 1-D
x2 = np.array([0, 1, 2])
st.write("Show 1-D numpy: ",x2)

# Creating 2-D
x3 = np.array([[0,1,2], [3,4,5], [6,7,8]])
st.write("Show 2-D numpy: ",x3)

# Creating 3-D ( this is not displayable on streamlit )
x4 = np.array([[[0,1,2], [3,4,5], [6,7,8]],
            [[ 9, 10, 11],[12, 13, 14],[15, 16, 17]],
            [[18, 19, 20],[21, 22, 23],[24, 25, 26]]])
st.write("Show 3-D numpy [0]: ",x4[0])
st.write("Show 3-D numpy [1]: ",x4[1])
st.write("Show 3-D numpy [2]: ",x4[2])

# Creating a 1-D array
x10 = np.array([0,1,2,3,4,5,6,7,8])
st.write("Show 1-D array of 10 elements: ", x10)

x10_matrix = x10.reshape((3,3))
st.write("Reshape of 10 elements to 3x3: ", x10_matrix)

array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

stack_2d = np.vstack((array1, array2))
st.write("Stack 2 individual arrays: ", stack_2d)

stacked = np.array([[1,2,3], [4,5,6]])
split_stack = np.split(stacked, 2)
st.write("split stacks: ", split_stack)


