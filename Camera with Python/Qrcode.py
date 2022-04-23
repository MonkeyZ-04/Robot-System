# Untitled - By: admin - พฤ. เม.ย. 21 2022

import sensor, image, time,lcd

lcd.init()
lcd.rotation(2)
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(time = 2000)

stock=[]
stopTag = 50

while(True):
    disPlay = image.Image(size=(320,240))
    img = sensor.snapshot()
    tag = img.find_apriltags()
    if tag :
        tagID = tag[0].id()
        img.draw_string(tag[0].x(),tag[0].y()-15,str(tagID),color=(0,0,255),size=2)
        img.draw_rectangle(tag[0].rect(),thickness=2,color=(0,255,0))
        if tagID >= stopTag:
            break
        if tagID not in stock :
            stock.append(tagID)
    if len(stock) ==3:
        break
    print('Finish')
    print(stock)
    writeY = 1
    for x in stock:
        disPlay.draw_string(img.width()+10,writeY*15,str(x),color=(255,255,255),size=1)
        writeY += 1
    disPlay.draw_image(img,5,5)
    lcd.display(disPlay)
print(stock)
print('Finish')
time.sleep(2)

while(True):
    disPlay = image.Image(size=(320,240))
    img = sensor.snapshot()
    tag = img.find_apriltags()
    if tag :
        tagID = tag[0].id()
        img.draw_string(tag[0].x(),tag[0].y()-15,str(tagID),color=(0,0,255),size=2)
        img.draw_rectangle(tag[0].rect(),thickness=2,color=(0,255,0))
        if tagID  in stock :
            stock.remove(tagID)
            print('Drop Box No.',tagID)
    print(stock)
    writeY = 1
    disPlay.draw_image(img,5,5)
    for x in stock:
        disPlay.draw_string(img.width()+10,writeY*15,str(x),color=(255,255,255),size=1)
        writeY += 1
    lcd.display(disPlay)
    if len(stock) ==0:
        break
