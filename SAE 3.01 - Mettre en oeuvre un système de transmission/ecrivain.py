import paho.mqtt.client as mqtt

BROKER = "192.168.1.25"
PORT = 1883
TOPIC = "maison/led/etat"
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
client.connect(BROKER, PORT, 60)
# Exemple : alterner entre ON et OFF toutes les 2 secondes
etat = "OFF"
while True:
    etat = "ON" if etat == "OFF" else "OFF"
    client.publish(TOPIC, etat)