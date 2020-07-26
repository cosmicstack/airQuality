from Adafruit_IO import Client
import serial, time

ser = serial.Serial('/dev/ttyUSB0')
aio = Client(username, adafruit_io_key)
print("Preparing Transmission")
#Wait until Internet Connection is Established
#Crontab starts at reboot
time.sleep(60)
print("Open Channel")

while True:
    data = []
    for i in range(0,10):
        line = ser.read()
        data.append(line)
    pmtwofive = int.from_bytes(b''.join(data[2:4]), byteorder='little')/10
    aio.send('apttwofive', pmtwofive)
    pmten = int.from_bytes(b''.join(data[4:6]), byteorder='little')/10
    aio.send('aptten', pmten)
    time.sleep(10)