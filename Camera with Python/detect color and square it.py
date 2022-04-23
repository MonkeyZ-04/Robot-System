# Untitled - By: admin - พ. เม.ย. 20 2022

import sensor, image, time,lcd

lcd.init()
lcd.rotation(2)

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)

colorThreshold = [(41, 83, -4, 39, -7, 24)]
while(True):
    img = sensor.snapshot()
    detectcolorcone=img.find_blobs(colorThreshold,area_threshold=200,pixels_threshold=200)
    #print(detectcolor)
    if detectcolorcone:
        for x in detectcolorcone:
            img.draw_rectangle(x[:4],color=(0,255,0),thinkness=2,color=(0,0,255))


