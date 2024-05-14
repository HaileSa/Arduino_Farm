# Bienvenue sur ✨ LaFerme ✨

Sur ce repository, vous trouverez :

  - Un dossier, avec le sketch récupérant la température et l'humidité à l'aide du capteur Arduino
  - Un dossier La_Ferme, avec trois fichiers :
          Ferme.py : Affiche le graphique matplotlib évolutif affichant les données récupérées, un dataframe et une alerte si le seuil est trop bas ou trop haut
          Tableau.py : Qui convertit les données en temps réel sur un tableau, toutes les secondes
          Donnees_temperature.csv : Le résultat du tableau 

## Utilisation

  - Brancher le capteur Arduino et vérifier le port sur l'IDE Arduino
  - Explorer les Données :
    - Lancer d'abord Ferme.py, puis Tableau.py. Le graphique s'affiche et se lance. Donnes_temperature.csv s'actualise et prend en compte les données prises sur le moment.
    - Pour afficher le dashboard : lancer streamlit avec streamlit run tableau.py
