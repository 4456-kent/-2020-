import time
import picamera

while(i<100):
    with picamera.PiCamera() as camera:
        camera.resolution=(1024,768)
        time.sleep(0.1)
        camera.capture('test_photo%d.jpg'%i+1)
    time.sleep(0.1)
