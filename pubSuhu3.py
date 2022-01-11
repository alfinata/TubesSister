# import library
import paho.mqtt.client as mqtt
import time, random

# fungsi saat publish
def on_publish(client, userdata, result):
    pass

# ceritanya fungsi mengambil suhu setempat
def getTemp():
    return round(random.uniform(20.00, 30.00), 2)

# buat client baru bernama P3
print("Sensor 3 menyala...")
client = mqtt.Client("P3")

# kaitkan callback on_publish ke client
client.on_publish = on_publish

# lakukan koneksi ke broker
print("Menghubungkan ke broker...")
client.connect("broker.emqx.io", port=1883)

# mulai loop client
client.loop_start()

# loop 20 kali
for i in range (6):

    # setiap 10 detik
    time.sleep(10)

    # ambil suhu
    temperature = getTemp()

    # publish data dengan topik = "sensor 3"
    client.publish("sensor_3", payload=temperature)

    # print saat berhasil publish
    print('Suhu yang terkirim ', temperature)

#stop loop
client.disconnect()
client.loop_stop()
print("Sensor 3 mati.")