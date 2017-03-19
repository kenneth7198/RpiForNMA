from SimpleCV import *
from operator import add

cam = SimpleCV.Camera()
disp = SimpleCV.Display()
frames_to_blur = 4
frames = ImageSet()

while disp.isNotDone():
    img = cam.getImage()
    p = img.scale(320,240)
    frames.append(p)

    if len(frames) > frames_to_blur:
        frames.pop(0)

    pic = reduce(add, [i/float(len(frames)) for i in frames])

    pic.show()
    
