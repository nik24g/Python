list=0
while 1:
    if list+1<100:
        list=list+1
        continue
    print(list,end=" ")

    if list+1==103:
        list=list+1
        break
    list = list + 1

while 1:
    inp=int(input("\npls enter the number "))
    if inp>100:
            print("congratulation You have enter the value greater than 100")
            break
    else:
        print("try again")
        continue
