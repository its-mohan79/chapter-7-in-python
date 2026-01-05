#break method


for i in range(100):
    if(i==35):
        break #exit the loop right now
    print(i)




#continue method


for i1 in range(100):
    if(i1==35):
        continue#skip the iteration
    print(i1)    


#example 1

for i3 in range(0, 80):
    print(i3)
    if i3 == 3:
        break
#example 2

for i4 in range(4):
    print("printing")
    if i4==2:
        continue
    print(i4)