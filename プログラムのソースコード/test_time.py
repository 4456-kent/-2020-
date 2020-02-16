import time
import csv
t0=time.time()
f=open("test_time.csv","w")
header=['TIME']
writer=csv.writer(f,lineterminator="\n")
writer.writerow(header)

i=0
while True:
    t=time.time()-t0
    TIME=[t]
    writer.writerow(TIME)
    time.sleep(0.1)
    i=i+1

    if (i==100):
        break

print("end\n")
f.close()
