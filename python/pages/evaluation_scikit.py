import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import streamlit as st

# Define the reference and LLM responses
# ref_response = ["The cat sat on the mat."]
ref_response = list(st.text_area('Enter Ref response', None))
# llm_response = ["The dog sat on the rug."]
llm_response = list(st.text_area('Enter LLM response', None))

if ref_response is not None and llm_response is not None:
    # Calculate the accuracy score
    accuracy = accuracy_score(ref_response, llm_response)
    st.write("Accuracy:", accuracy)

    # Calculate the precision score
    precision = precision_score(ref_response, llm_response, average="weighted")
    st.write("Precision:", precision)

    # Calculate the recall score
    recall = recall_score(ref_response, llm_response, average="weighted")
    st.write("Recall:", recall)

    # Calculate the F1 score
    f1 = f1_score(ref_response, llm_response, average="weighted")
    st.write("F1 Score:", f1)

    # Calculate the confusion matrix
    confusion_mat = confusion_matrix(ref_response, llm_response)
    st.write("Confusion Matrix:\n", confusion_mat)