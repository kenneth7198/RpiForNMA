import SimpleCV

cam = SimpleCV.Camera()
disp = SimpleCV.Display()


while disp.isNotDone():
    img = cam.getImage()
    p = img.scale(320,240)
    screensize = p.width * p.height
    
    min_blob_size = 0.10 * screensize
    max_blob_size = 0.80 * screensize
    blobs = p.findBlobs(minsize=min_blob_size, maxsize=max_blob_size)

    if blobs:
        print(blobs)
    
    p.show()
    
