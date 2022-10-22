import serial
import time
import sys
import threading



try:
    host = serial.Serial(port = 'COM7', baudrate = 9600,
                    parity = serial.PARITY_NONE,
                    stopbits = serial.STOPBITS_ONE,
                    bytesize = serial.EIGHTBITS)
    print('Established serial connection to GMC1200')
    host.timeout = 1  #시리얼에 데이터를 불러올 때 지정하는 딜레이
except:
    print("Device can not be found or can not be configured")
    sys.exit(0)




while True:
    host_cmd = input("input : ").strip()
    if host_cmd =='done':
        print('finished program')
        break
    host.write(host_cmd.encode())
    time.sleep(0.5)
    print(host.readline().decode('ascii'))

host.close()