import SimpleCV

cam = SimpleCV.Camera()
disp = SimpleCV.Display()

while disp.isNotDone():
    img = cam.getImage()
    img2 =SimpleCV.Image('pi.png')
    #img3 = img + img2
    img2.show()
 
