import SimpleCV

cam = SimpleCV.Camera()
disp = SimpleCV.Display()

while disp.isNotDone():
    img = cam.getImage()
    crop = img.crop(150,200,100,100)
    crop.show()
