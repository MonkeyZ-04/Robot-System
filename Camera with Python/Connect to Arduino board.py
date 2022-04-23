# Untitled - By: admin - พ. เม.ย. 20 2022

import sensor, image, time,lcd,math
from machine import I2C
from fpioa_manager import fm
from Maix import GPIO

lcd.init()
lcd.rotation(2)

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)

i2c = I2C(I2C.I2C0,freq=100000,scl=32,sda=34)



laneColor = [(100, 88, -8, -128, 96, 48)]
h1Cut = [(80, 100, -10, 10, -10, 10)]               #ค่าสีแสงสะท้อน
def motorControl(speedL,speedR):
    i2c.writeto(0x12,bytes([int(speedL+127),int(speedR+127)]))

motorControl(50,50)
time.sleep(10)
motorControl(0,0)

while(True):
    img = sensor.snapshot()
    img.binary(h1Cut,zero=True)
    #lane=img.find_blobs(laneColor,area_threshold=200,pixels_threshold=120)
    laneline = img.get_regression(laneColor,area_threshold=200,pixels_threshold=200)
    if laneline:
        img.draw_line(laneline.line(),thickness=2,color=(0,255,0))
        #for x in lane:
            #img.draw_rectangle(x[:4],color=(0,255,0),thinkness=2,color=(0,0,255))
    lcd.display(img)




