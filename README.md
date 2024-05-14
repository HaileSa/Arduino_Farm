# Bienvenue sur ✨ LaFerme ✨

Le but de se projet est de récupérer et d'afficher la température et l'humidité en temps réel à l'aide d'un capteur Arduino Nano 33.
Nous avons fait un graphique evolutif, ainsi qu'un tableau csv et d'un dashboard streamlit. 
De plus, un seuil de température et d'humidité a été mis en place, en dehors duquel s'affiche une pop-up d'alerte disant qu'il fait trop chaud/froid ou sec/humide.

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
