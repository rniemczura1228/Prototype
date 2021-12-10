def total(a,b):
    global result
    result=a+b 

def openFile(filename,mode):
    global f
    f = open(filename,mode)

def writeLine(line):
    f.write(line)

def closeFile():
    f.close()

def main():

    # Number Function
    a = 5
    b = 7
    total(a,b)
    print(" Sum of ",a,"and"," sun of ",b,"result ", result)

    # Write to file
    filename = "workfile.txt"
    mode = "a+"
    openFile(filename,mode)
    for i in range(10):
       line = "This is line " + str(i) + "\n"
       writeLine(line)
    closeFile()
    
if __name__== "__main__" :
        main()
