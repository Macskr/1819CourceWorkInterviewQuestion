import time


data = {}

def readataset():
    start = time.time()
    filename = input("input name of file containing data (with extension)")
    d = open(filename, 'r')  # opening the generated file
    for l in d:
        key = eval(l.split(":")[0])
        val = eval(l.split(":")[1])
        x = { key:val}
        data.update(x)
    print("timetaken:", time.time() - start)

readataset()
#print(data)
