
import serial
import matplotlib.pyplot as plt
import tkinter as tk
import streamlit as st
    
arduino = serial.Serial(port='COM7', baudrate=115200, timeout=.1)

# INITIALISATION DES VALEURS
temperatures = []
humidities = []
seuil_min_temperature = 25
seuil_max_temperature = 33
seuil_min_humidity = 20
seuil_max_humidity = 50



fig = plt.figure()

line1, = plt.plot(temperatures,color='pink',label='temperature')
line2, = plt.plot(humidities,color='purple',label='humidité')
plt.ion()
plt.show()

popup = tk.Tk()
popup.withdraw()  # Masquer la fenêtre principale


alert_displayed = False  

def show_alert(message):
    global alert_displayed 
    
    if not alert_displayed:
        popup.deiconify()
        popup.title("Alerte")
        popup.geometry(f"{400}x{300}")
        popup.configure(bg="pink")
        label = tk.Label(popup, text=message, foreground="black", anchor="center")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(popup, text="OK", command=popup.withdraw)
        button.pack()
        popup.update()
        alert_displayed = True


while True:
   
    data =arduino.readline().decode("utf-8")
    if data == "":
        continue
    data = data.split(",")
   
    # print(temperatures)


    temperature = float(data[0])
    humidity = float(data[1])

    # ça ça ajoute la data au tableau
    temperatures.append(temperature)
    humidities.append(humidity)

    import pandas as pd

    # Créer un DataFrame à partir des listes de températures et d'humidités
    df = pd.DataFrame({'Temperature': temperatures, 'Humidity': humidities})

    # Enregistrer le DataFrame dans un fichier CSV
    df.to_csv('donnees_temperature.csv', index=False)


    # Réinitialiser l'alerte affichée lorsque la condition n'est plus remplie
    if temperature <= seuil_max_temperature and humidity <= seuil_max_humidity:
        alert_displayed = False

    #réglage des seuils
    if temperature > seuil_max_temperature :
        show_alert(f"TEMPERATURE HAUTE ! Qué calor, arrose les plantes : {temperature}")

    if humidity > seuil_max_humidity :
        show_alert(f"HUMIDITE HAUTE ! Sors ton parapluie  : {humidity}")

    if temperature < seuil_min_temperature :
        show_alert(f"TEMPERATURE BASSE ! Qué frio, réchauffer la serre : {temperature}")

    if humidity < seuil_min_humidity :
        show_alert(f"HUMIDITE BASSE ! C'est sec, arrose les plantes  : {humidity}")


    # ca c'est la température
    fig
    line1.set_ydata(temperatures)
    line1.set_xdata(range(len(temperatures)))
    fig.axes[0].set_ylim(20,(max(humidities)+10))
    fig.axes[0].set_xlim(0, len(temperatures))
    fig.canvas.draw()
    fig.canvas.flush_events()

    # ca c'est l'humidité
    line2.set_ydata(humidities)
    line2.set_xdata(range(len(humidities)))
    fig.axes[0].set_xlim(0, len(humidities))


    fig.canvas.draw()
    fig.canvas.flush_events()


    plt.title('Température et humidité en tps réel')
    plt.legend(loc='upper left')
    plt.pause(1.0)
