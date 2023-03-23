import serial

from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
 

# dd/mm/YY H:M:S
dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S\r\n"))
#dt_string = "hello rpi\r\n"
print(dt_string)
ser = serial.Serial(
        port='/dev/ttyUSB0', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)
print(ser.name)         #check which port was really used
ser.write(dt_string.encode())
ser.close()             #close port

