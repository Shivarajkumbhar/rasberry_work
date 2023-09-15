from gpiozero import button
from time import sleep
btn = button(4)
if btn.is_pressed:
  print('button is pressed')
  sleep(1)
