# for loop is used to complete the iteration or repeating the task
name=input("Enter your name")
#iterate name using for loop
# e.g in c for(int i=0;i<10;i++)
for i in name:
    print(i)

    # print the no. 1 to 10
    for x in range(1,11):
        print(x)

 #print this pattern using for loop 1,3,5,7,9,11 solve by step size
for x in range(1,12,2):
    print(x)

    #print this pattern using for loop 1,3,5,7,9,11 solve without by step size
for i in range(1,12):
    if i % 2!=0:
        print(i)

        #print the even  no. using for loop 1 to 20
        for i,in range(1,21):
            if i % 2 == 0:
                print(i)
            else:
                print(i)