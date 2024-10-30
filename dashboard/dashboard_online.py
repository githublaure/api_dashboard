import streamlit as st
import pandas as pd
import requests  # Pour faire des requêtes HTTP
import matplotlib.pyplot as plt

# Remplacez par l'adresse publique de votre instance EC2
API_URL = "http://3.222.37.118/"

# Chargement du dataset localement pour afficher les notes
df = pd.read_csv('../data/processed/data_test.csv')

# Titre du dashboard
st.title('Scores des Élèves')

# Sélectionner l'élève
eleve_select = st.selectbox('Choisissez un Élève:', df['Élève'])

# Obtenir la note de l'élève sélectionné
note_eleve = df.loc[df['Élève'] == eleve_select, 'Notes'].values[0]

# Appeler l'API pour obtenir la moyenne
response = requests.get(f"{API_URL}/score")
if response.status_code == 200:
    data = response.json()
    moyenne = data['moyenne']  # La moyenne renvoyée par l'API
else:
    st.error("Erreur lors de l'appel à l'API")

# Afficher les résultats
st.write(f"La note de **{eleve_select}** est : **{note_eleve}**")
st.write(f"La moyenne des notes est : **{moyenne}**")

# Affichage du barplot
plt.bar(df['Élève'], df['Notes'], color='skyblue')
plt.axhline(y=moyenne, color='red', linestyle='--', label='Moyenne')
plt.axhline(y=note_eleve, color='green', linestyle='--', label=f'Note de {eleve_select}')
plt.xlabel('Élève')
plt.ylabel('Notes')
plt.title('Notes Scolaires')
plt.legend()

# Affichage du graphique
st.pyplot(plt)
