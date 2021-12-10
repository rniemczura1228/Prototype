def total(a,b):
   global result
   result=a+b 

def main():
    print("Hello, World!")
    a= int(input("Enter first number:"))
    b= int(input("Enter second number:"))
    total(a,b)#funtion call the 2 integer
    print(" Sum of ",a,"and"," sun of ",b,"result ", result)
    total(5,7)
    print(" Sum of ",a,"and"," sun of ",b,"result ", result)
    
if __name__== "__main__" :
        main()
