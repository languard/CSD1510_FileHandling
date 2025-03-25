import random

rndOutput = open("lectureFile.txt", "w")
random.seed()

for _ in range(50000):
    rndOutput.write(str(random.randint(1,20)))
    rndOutput.write("\n")

rndOutput.close()
print("Done creating numbers")


rndInput = open("lectureFile.txt")

sum = 0
count = 0
oneCount = 0
twentyCount = 0
evenCount = 0
oddCount = 0

for curLine in rndInput:
    tempInt = int(curLine)
    count += 1
    sum += tempInt
    if tempInt % 2 == 0:
        evenCount += 1
    else:
        oddCount += 1
    if tempInt == 1:
        oneCount += 1
    if tempInt == 20:
        twentyCount += 1
    
rndInput.close()

avg = sum / count

print(f"The sum is {avg}.")
print(f"The number of evens is {evenCount} and odds is {oddCount}.")
print(f"The number of 1's is {oneCount} with expected being {count / 20}") #1 in twenty chance
print(f"The number of 20's is {twentyCount} with expected being {count / 20}") #1 in twenty chance
    

