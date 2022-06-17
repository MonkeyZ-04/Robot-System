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



laneColor = [(92, 99, -27, -5, 18, 89)]
h1Cut = [(80, 100, -10, 10, -10, 10)]#ค่าสีแสงสะท้อน
Cone = [(43, 87, 16, 66, -12, 37)]
old_cx_normal = 0
def motorControl(speedL,speedR,speedL1,speedR1):
    i2c.writeto(0x12,bytes([int(speedL+127),int(speedR+127), int(speedL1+127),int(speedR1+127)]))

def sw_OK_press():
    while True:
        swOK = i2c.readfrom(0x12,1)
        if int(swOK[0]) ==1 :
            break

def getError(showLine):
        global old_cx_normal
        cy = img.height() / 2
        cx = (laneline.rho() - (cy * math.sin(math.radians(laneline.theta())))) / math.cos(math.radians(laneline.theta()))
        cx_middle = cx - (img.width() /2)
        cx_normal = cx_middle / (img.width() /2)
        if old_cx_normal != None :
            old_cx_normal = (cx_normal * 0.9) + (old_cx_normal * 0.1)
        else :
            old_cx_normal = cx_normal
        #print(old_cx_normal)
        if showLine and laneline:
            img.draw_line(laneline.line(),thickness=2,color=(0,255,0))
        return old_cx_normal

def findCone(inputImage,detectArea):
    if inputImage :
        detectCone = inputImage.find_blobs(Cone,area_threshold=detectArea,pixels_threshold=int(detectArea*0.6))
           #0.7 = ในจอมีกรวยกี่เปอร์เซ็น 0.7 = 70
        #print(detectCone)
        if detectCone :
            return detectCone[0].cx()
    else:
        return 0

sw_OK_press()
lastError = 0
Kp = 20
Kd = 9
nSpeed = 20
#motorControl(50,50)
#time.sleep(2)
#motorControl(0,0)


while(True):
    img = sensor.snapshot()
    img.binary(h1Cut,zero=True)
    laneline = img.get_regression(laneColor,area_threshold=200,pixels_threshold=200)
    print(findCone(img,2000))
    coneNaja = findCone(img,7200)
    if coneNaja :
        if coneNaja <= (img.width()//2)-25:
            motorControl(0,0,0,0) #หลบขวา
            time.sleep(0.5)
            motorControl(30,-30,30,-30)
            time.sleep(1.5)
            motorControl(30,30,30,30)
            time.sleep(2)
            motorControl(-30,30,-30,30)
            time.sleep(1.5)
        elif coneNaja >= (img.width()//2)-25:
            motorControl(0,0,0,0) #หลบซ้าย
            time.sleep(0.5)
            motorControl(-30,30,-30,30)
            time.sleep(1.5)
            motorControl(30,30,30,30)
            time.sleep(2)
            motorControl(30,-30,30,-30)
            time.sleep(1.5)
        else : #ตรงกลาง
            motorControl(0,0,0,0) #หลบขวา
            time.sleep(0.5)
            motorControl(30,-30,30,-30)
            time.sleep(1.5)
            motorControl(30,30,30,30)
            time.sleep(2)
            motorControl(-30,30,-30,30)
            time.sleep(1.5)
    elif laneline:
        error = getError(True)
        PDValue = (Kp * error)+(Kd*(error - lastError))
        lastError = error
        leftpower = nSpeed + PDValue
        rightpower = nSpeed - PDValue
        if leftpower > 100:
            leftpower = 100
        if rightpower > 100:
            rightpower = 100
        if leftpower < -100:
            leftpower = -100
        if rightpower < -100:
            rightpower = -100
        motorControl(leftpower,rightpower,rightpower,leftpower)
    elif laneline ==0:
        m
    else :
        motorControl(0,0,0,0)
    lcd.display(img)

