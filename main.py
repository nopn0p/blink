from os import sys 
from os import system 
import time

led_interval = 0.01
bit_interval = 0.03
byte_interval = 0.06

def led(state): 
    if state == 1: 
        led = open(sys.argv[2], 'w')
        led.write("1") 
        led.close()
        time.sleep(led_interval)
    else: 
        led = open(sys.argv[2], 'w') 
        led.write("0")
        led.close() 
        time.sleep(led_interval)

def transmit(byte): 
    parity = byte.count("1") 
    if parity % 2 == 0: 
        parity = "1" 
        # the amount of 1-bits is even 
    else: 
        parity = "0" 
        # the amount of 1-bits is odd 
    byte = byte + parity
    for bit in byte: 
        if bit == "1": 
            print("1 detected - flashing") 
            # 2 flashes for 1-bit 
            led(1)
            led(0)
            led(1)
            led(0) 
            time.sleep(0.3)
        else: 
            print("0 detected - flashing") 
            # 1 flash for 0-bit 
            led(1)
            led(0)
            time.sleep(0.3)

def main(): 
    bytecount = 0 
    start = time.time()
    f = open(sys.argv[1]) 
    for line in f: 
        i = [x[2:] for x in list(map(bin, bytearray(line, 'utf-8')))]
        for j in i: 
            print(j)
            print("=====")
            transmit(j)
            print("Transmitted 1 complete byte.") 
            bytecount += 1 
            time.sleep(byte_interval)
    print("Transmitted %s bytes in %s seconds." % (bytecount, (time.time() - start))) 
    print("Bitrate: %s" % (bytecount*8/(time.time() - start)))
main() 

