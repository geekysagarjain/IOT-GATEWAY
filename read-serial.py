import serial
import time

ser = serial.Serial('/dev/ttyUSB0')
ser.baudrate = 9600
ser.timeout = 2
print (ser.is_open)

if ser.is_open:
    while True:
        fh = open("/home/pi/serial-data.txt", "a+")
        size = ser.inWaiting()
        if size:
          res = ser.read()
          hmr = res.decode("Ascii")
          print(hmr)
          fh.write(hmr)
        else:
          print ("no data")
          fh.close
          time.sleep(1)
else:
    print ("serial not open")

