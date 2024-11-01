import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Chargement du dataset
df = pd.read_csv('../data/processed/data_test.csv')

# Titre du dashboard
st.title('Scores des Élèves')

# Sélectionner l'élève
eleve_select = st.selectbox('Choisissez un Élève:', df['Élève'])

# Obtenir la note de l'élève sélectionné
note_eleve = df.loc[df['Élève'] == eleve_select, 'Notes'].values[0]

# Calculer la moyenne
moyenne = df['Notes'].mean()

# Afficher les résultats
st.write(f"La note de **{eleve_select}** est : **{note_eleve}**")
st.write(f"La moyenne des notes est : **{moyenne}**")

# Affichage du barplot
plt.bar(df['Élève'], df['Notes'], color='skyblue')

# Mettre en évidence la note de l'élève sélectionné
plt.axhline(y=moyenne, color='red', linestyle='--', label='Moyenne')
plt.axhline(y=note_eleve, color='green', linestyle='--', label=f'Note de {eleve_select}')

plt.xlabel('Élève')
plt.ylabel('Notes')
plt.title('Notes Scolaires')
plt.legend()

# Affichage du graphique
st.pyplot(plt)
