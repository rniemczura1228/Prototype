#Assign the filename
filename = "basket.txt"
# Open file for writing
fileHandler = open(filename, "r")
numfruit = 0
idx = 0
type = ["fruit"]
count = [0,0,0,0,0,0,0,0,0]
#fruits = ['type']
#fruits.append("orange") 

# Read a file line by line
for line in fileHandler:
  numfruit = numfruit + 1
  x = line.split(",")
  if x[0] not in type:
     type.append(x[0])
  i = 0
  while i < len(type):
     if (x[0] != 'fruit'):
        if (x[0] == type[i]):
            xint = int(x[1])
            count[i] = count[i] + xint
     i += 1
 
# deduct row titles for fruit count
numfruit = numfruit - 1

# Close the file amd print counts
print('Number of pieces of fruit = ', numfruit)
print('Number of types of fruit = ', len(type))
print('Types', type)
print('Counts', count)
type.remove('fruit')
type.sort()
print('Sorted fruit types list ', type)
print('Counts', count)

fileHandler.close()