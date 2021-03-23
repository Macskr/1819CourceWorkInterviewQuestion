import time

''' Bubble sort base template taken from https://github.com/vptuan/COMP1819ADS/tree/main/Lab_05'''
data = {}
indivset = []



def WriteSorted2FIle():
    file = input("input file name")
    with open((file + "_Sorted" + ".txt"), 'w') as f:
        for i in indivset:
            f.write("%s\n" % i)


def readatadict():
    # start = time.time()
    filename = input("input name of file containing data (with extension)")
    d = open(filename, 'r')  # opening the generated file
    for l in d:
        key = eval(l.split(":")[0])
        val = eval(l.split(":")[1])
        x = {key: val}
        data.update(x)
    # print("timetaken:", time.time() - start)


def convtollst(data):
    for key in data:
        if int(((key)[1])) > 40:
            x = 1
        else:
            x = 0
        indivset.append([key, (len(data[key])) + x])


def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    swapFlag = False
    for i in range(n):
        # print("Pass iter:", i)
        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element

            if (arr[j])[1] > (arr[j + 1])[1]:  # check for the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapFlag = True
                # print("Swap.. : ", arr[j + 1], arr[j], arr)

        if (swapFlag == False):
            break

# Function to do insertion sort
start = time.time()
# Converting the dictionary into a usable set
readatadict()
# Generating a set of with risk factor calculated
convtollst(data)
# Sorting the Final Set
bubble_sort(indivset)
print("timetaken:", time.time() - start)
WriteSorted2FIle()

'''
print(indivset) #a set containing all individuals [(name , age , ID number), risk factor] , .....
print(indivset[0]) #one individual with risk factor [(name , age , ID number), risk factor]  
print(((indivset[0])[0]))# one individual without risk factor  (name , age , ID number)
print(((indivset[0])[0])[0]) #name 
print(((indivset[0])[0])[1]) #age 
print(((indivset[0])[0])[2]) #ID Number
'''
