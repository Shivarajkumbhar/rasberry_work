from gpiozero import button
from time import sleep
btn = button(4)
if btn.is_pressed:
  print('button is pressed')
  sleep(1)


#led on when button preesed

from gpiozero import Button
from time import sleep
from gpiozero import LED
btn = Button(4)
led = LED(2)
led.off()
	if btn.is_pressed:
		print('Btn pressed')
		led.on
		sleep(1)
	else:
		led.off
