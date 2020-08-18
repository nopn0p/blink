## blink: bypassing airgaps by flashing LEDs 
This is a fun little afternoon project that I decided to do because I was reminded of the existence of [LEDitgo](https://cyber.bgu.ac.il/advanced-cyber/system/files/LED-it-GO_0.pdf), so I wanted to see how easy this would be to implement in python at a much lower scale. 
(spoiler alert, it's easy)

### usage
Transmitting text file through HDD activity LED on HP laptop running Arch Linux: 
```sudo python main.py test.txt /sys/class/leds/hp\:\:hddprotect/brightness```

### configuration 
You can set 3 values in main.py: `led_interval`, `bit_interval` and `byte_interval`. 
1. `led_interval` determines the time that passes between each activation/deactivation of the LED. 
2. `bit_interval` determines the time that passes between the transmission of each bit. 
3. `byte_interval` determines the time that passes between the transmission of each byte. 

### references 

