import time
import picamera

while(i<10):
    with picamera.PiCamera() as camera:
        camera.resolution=(1024,768)
        time.sleep(0.1)
        camera.capture('test_photo%03d.jpg'%i+1)
    time.sleep(0.1)
    i+=1
