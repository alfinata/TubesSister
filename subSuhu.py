# import paho mqtt
import paho.mqtt.client as mqtt
import time

# penyimpanan total suhu
totalSuhu = []

# fungsi saat menerima message
def on_message(client, userdata, message):
    totalSuhu.append(float(message.payload.decode("utf-8")))
    if len(totalSuhu)%3 == 0:
        a = totalSuhu[len(totalSuhu)-1]
        b = totalSuhu[len(totalSuhu)-2]
        c = totalSuhu[len(totalSuhu)-3]
        tot = a+b+c
        print(f"Suhu bandung: {round(tot/3, 2)}")

# buat client baru bernama P4
print("Bandung Weather News menyala...")
client = mqtt.Client("P4")

# kaitkan callback on_message ke client
client.on_message = on_message

# buat koneksi ke broker
print("Menghubungkan ke broker...")
client.connect("broker.emqx.io", port=1883)

# jalankan loop client
client.loop_start()

# print topik yang disubscribe (dalam konteks ini, 3 sensor suhu)
print("Subscribing to 3 sensors")

# loop
for i in range(70):

    # berikan waktu tunggu 1 detik
    time.sleep(1)

    # subscribe ke setiap sensor
    client.subscribe("sensor_1")
    client.subscribe("sensor_2")
    client.subscribe("sensor_3")

#stop loop
client.disconnect()
client.loop_stop()
print("Sistem Bandung Weather News mati.")