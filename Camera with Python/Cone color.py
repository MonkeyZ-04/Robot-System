# Untitled - By: admin - Fri Apr 22 2022

import sensor, image, time,lcd

lcd.init()
lcd.rotation(2)
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)

colorThreshold = (43, 87, 16, 66, -12, 37)

while(True):
    img = sensor.snapshot()
    lcd.display(img)
