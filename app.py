# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import string
import warnings
warnings.filterwarnings('ignore')
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, precision_score, recall_score
import streamlit as st
import pickle



with open("data.pkl", "rb") as file:
    model = pickle.load(file)



st.title("HOTEL REVIEW SENTIMENT ANALYSIS")

comment = st.text_area("Leave your comment here:")

if st.button("Submit"):
    # When the button is clicked, display the comment
    if comment:
        st.write("Your comment:")
        prediction=model.predict([comment])
        st.write(prediction[0])
    else:
        st.write("Please enter a comment before submitting.")