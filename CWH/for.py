a=['Aryan','Pratik','Varun','Pritam','Vaibhav','Prassana']

#************Using While loop*************
i=0
while i<len(a):
        print(a[i])
        i=i+1

        #************Using For loop*************
for item in a:
    print(item)

#************Using for loop Specific range*************
for item in range(1,4): #(start,stop,step size)
    print(item)
for item in range(2,11,2): #(start,stop,step size)
    print(item)

#************Using for loop else*************
for item in range(5): 
    print(item)
else:
        print("done with 5 number")

#************Using for loop Break*************
for item in range(15): 
    print(item)
    if item==5:
        break