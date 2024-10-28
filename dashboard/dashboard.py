import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Chargement du dataset
df = pd.read_csv('data/processed/data_test.csv')

st.title('Scores des Élèves')

# Affichage du barplot
plt.bar(df['Élève'], df['Notes'])
plt.xlabel('Élève')
plt.ylabel('Notes')
plt.title('Notes Scolaires')
st.pyplot(plt)
