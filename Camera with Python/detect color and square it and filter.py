# Untitled - By: admin - พ. เม.ย. 20 2022

import sensor, image, time,lcd

lcd.init()
lcd.rotation(2)

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)

colorThreshold = [(100, 88, -8, -128, 96, 48)]
h1Cut = [(80, 100, -10, 10, -10, 10)]               #ค่าสีแสงสะท้อน
while(True):
    img = sensor.snapshot()
    img.binary(h1Cut,zero=True)
    detectcolor=img.find_blobs(colorThreshold,area_threshold=200,
    pixels_threshold=200)
    print(detectcolor)
    if detectcolor:
        for x in detectcolor:
            img.draw_rectangle(x[:4],color=(0,255,0),thinkness=2,color=(0,0,255))
    lcd.display(img)




