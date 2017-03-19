import SimpleCV

cam = SimpleCV.Camera(0,{"width":320,"height":240})
disp = SimpleCV.Display((320,240))
#cam.live()

while disp.isNotDone():
    img = cam.getImage().colorDistance((207,203,101)).invert()
    p = img.scale(320,240)
    screensize = p.width * p.height
    minsizeBlob = 0.10 * screensize
    maxsizeBlob = 0.60 * screensize
    b = p.findBlobs(minsize = minsizeBlob, maxsize = maxsizeBlob)
    
    if b:
        b.draw((255,0,0))
        print("Blobs:"+str(b.count())+",largest blob at:"+str(b[-1].x)+","+str(b[-1].y))
        b[-1].drawRect(color=(0,0,255))
        
    p.show()
    
