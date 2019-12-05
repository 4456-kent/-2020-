import csv

f=open("test.csv","w")
i=0

while (i<100):
    h=i*100+50
    ih=[i,h]

    print(ih)
    
    writer=csv.writer(f,lineterminator="\n")
    writer.writerow(ih)

    i=i+1

print("end")
f.close()

