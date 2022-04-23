#scanไม่ครบอย่าออก
import sensor, image, time, lcd
from machine import UART
from fpioa_manager import fm
from Maix import GPIO

lcd.init()
lcd.rotation(2)
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(time = 2000)

fm.register(34,fm.fpioa.UART1_TX)
fm.register(32,fm.fpioa.UART1_RX)
uart_A = UART(UART.UART1, 115200, 8, None, 1, timeout=1000, read_buf_len=4096)

stock = []
stockIndex = []
stopTag = 50
#
while(True):
    display = image.Image(size=(320,240))
    img = sensor.snapshot()
    tag = img.find_apriltags()
    if tag :
        tagID = tag[0].id()
        img.draw_string(tag[0].x(),tag[0].y() - 15,str(tagID),color=(0,0,255),size=1)
        img.draw_rectangle(tag[0].rect(),thickness=2,color=(0,255,0))
        if tagID == stopTag :
            break
        if tagID not in stock :
            stock.append(tagID)
            stockIndex.append(len(stock))
    print(stock)
    display.draw_image(img,5,5)
    writeY = 1
    for x in stock :
        display.draw_string(img.width() + 10,writeY*15,str(x),color=(255,255,255),size=1)
        writeY += 1
    lcd.display(display)
    if len(stock) == 5:
        break

print(stock)
print("Finish")
time.sleep(5)
#Running
while(True):
    display = image.Image(size=(320,240))
    img = sensor.snapshot()
    tag = img.find_apriltags()
    if tag :
        tagID = tag[0].id()
        img.draw_string(tag[0].x(),tag[0].y() - 15,str(tagID),color=(0,0,255),size=1)
        img.draw_rectangle(tag[0].rect(),thickness=2,color=(0,255,0))
        if tagID in stock :
            indexID = stockIndex[stock.index(tagID)]
            uart_A.write(str(stockIndex[stock.index(tagID)]))
            stock.remove(tagID)
            stockIndex.remove(indexID)
            print("Drop box no.",tagID)
    print(stock)
    display.draw_image(img,5,5)
    writeY = 1
    for x in stock :
        display.draw_string(img.width() + 10,writeY*15,str(x),color=(255,255,255),size=1)
        writeY += 1
    lcd.display(display)
