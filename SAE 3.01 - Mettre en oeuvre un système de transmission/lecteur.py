import paho.mqtt.client as mqtt

BROKER = "lumenyana.local"
PORT = 1883
TOPIC = "prise1/etat"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    etat = msg.payload.decode()

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.loop_forever()
