import image,lcd

lcd.init()
lcd.rotation(2)
img = image.Image(size=(320,240))
img.draw_circle(160,120,120,color=(100,0,100),thickness=8,fill=True)
img.draw_cross(160,120,color=(255,255,255),thickness=2,size=120)
img.draw_string(30,90,"Hello World",color=(255,255,255),scale=5)
lcd.display(img)
