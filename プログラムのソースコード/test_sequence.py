import time

sequence='Phase1'

count=0

while(sequence=='Phase1'):
    print(sequence)
    print(" ")
    print(count)
    print("\n")
    if(count<100):
        count=count+1

    elif(count==100):
        sequence='Phase2'
        count=0
        break

    time.sleep(0.5)

while(sequence=='Phase2'):
    print(sequence)
    print(" ")
    print(count)
    print("\n")
    if(count<100):
        count=count+1

    elif(count==100):
        sequence='End'
        break

    time.sleep(100)

if(sequence=='End'):
    print(sequence)



