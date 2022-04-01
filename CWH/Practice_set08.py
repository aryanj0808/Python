def maximum(num1, num2, num3):
    if(num1>num2):
        if(num1>num3):
            return num1 
        else:
            return num3

    elif(num2>num3):
            return num2
    else:
        return num3

m=maximum(23,45,3)

print("Maximum number is : "+str(m))

def fahrenheit(Cel):
    return (Cel*9/5) + 32 

Cel=fahrenheit(1)
print(str(Cel))