import microchip_lora_modem as lora

uart_bt = pyb.UART(1,9600)

count = 0
time_out = 900000  # 15min
lora.connect_lora()
rtc = pyb.RTC()
rtc.wakeup(time_out) # wake every 30s


while True:
    pyb.LED(4).on()
    lora.send_message('pkg: '+str(count))
    uart_bt.write('pkg: '+str(count)+'\n')
    count +=1
    pyb.LED(4).off()
    if pyb.USB_VCP().isconnected():
        pyb.delay(time_out)
    else:
        pyb.stop()
