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


# Function to do insertion sort
def insertion_sort(arr):

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position

        j = i - 1
        while j >= 0 and key[1] < (arr[j])[1]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


start = time.time()
# Converting the dictionary into a usable set
readatadict()
# Generating a set of with risk factor calculated
convtollst(data)

# Sorting the Final Set
insertion_sort(indivset)
print("timetaken:", time.time() - start)
WriteSorted2FIle()
