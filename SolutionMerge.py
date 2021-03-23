import time

''' Merge sort base template taken from https://www.geeksforgeeks.org/merge-sort/'''
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

def mergeSort(arr):

    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if (L[i])[1] < (R[j])[1]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

start = time.time()
# Converting the dictionary into a usable set
readatadict()
# Generating a set of with risk factor calculated
convtollst(data)
# Sorting the Final Set
mergeSort(indivset)
print("timetaken:", time.time() - start)
WriteSorted2FIle()