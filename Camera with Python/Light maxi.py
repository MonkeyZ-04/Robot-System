from fpioa_manager import fm
from Maix import GPIO
import time

while(True):
    time.sleep(1)
    fm.register(14, fm.fpioa.GPIO0)
    led_r=GPIO(GPIO.GPIO0, GPIO.OUT)
    led_r.value(0)
    time.sleep(1)
    fm.register(13, fm.fpioa.GPIO0)
    led_r=GPIO(GPIO.GPIO0, GPIO.OUT)
    led_r.value(0)
    time.sleep(1)
    fm.register(12, fm.fpioa.GPIO0)
    led_r=GPIO(GPIO.GPIO0, GPIO.OUT)
    led_r.value(0)
    time.sleep(1)
    fm.register(11, fm.fpioa.GPIO0)
    led_r=GPIO(GPIO.GPIO0, GPIO.OUT)
    led_r.value(0)
