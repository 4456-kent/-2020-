import time
import picamera

for i in range(0,10):
    with picamera.PiCamera() as camera:
        camera.resolution=(1024,768)
        time.sleep(0.1)

        file_name='test_photo'+str(i+1)+'.jpg'
        camera.capture(file_name)
