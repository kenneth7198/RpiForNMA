import SimpleCV

cam = SimpleCV.Camera(0, {"width":320,"height":240})
disp = SimpleCV.Display((320,240))


while disp.isNotDone():
    img = cam.getImage()
    img.show()
