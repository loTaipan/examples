from ds18x20 import DS18X20
import microchip_lora_modem as lora
from pyb import Pin

time_out = 900000

debug = True

temp_sens = DS18X20(Pin('X5'))
lora.connect()

def measure_and_send():
	temp = int(temp_sens.read_temp()*100)
	byte1 = temp >> 8
	byte2 = temp & 0xff
	msg = "%02x" % byte1 +"%02x" % byte2
	lora.send_message_raw(msg)

while True:
	pyb.LED(4).on()
	measure_and_send()
	pyb.LED(4).off()
	lora.sleep(time_out-1000)
	pyb.delay(time_out)


