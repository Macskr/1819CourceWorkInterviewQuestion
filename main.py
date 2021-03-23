import random


def GenerateDataSet(n, factors):
    dictTMP = {}  # declaring a temporary dictionary
    Names = []  # list of available names
    Namefile = open('Names.txt', 'r')  # opening the Name file
    # For loop generates a list of names with no new line charn
    for l in Namefile:
        Names.append(l.strip('\n'))

    # for loop which repeats N times meaning Lenth(DataDict) = N
    for i in range(n):
        while True:
            lenbefore = len(dictTMP)
            ''' Name is now a set which also contains the age '''
            tmpIndiv = tuple(
                [Names[random.randint(0, (len(Names) - 1))], random.randint(0, 100), random.randint(0, 9999999)])
            # tmpIndiv = { Names[random.randint(0, (len(Names) - 1))] } # selects random name and assigns to var

            tmpVuln = set()  # declares a set which will contain Vulnerabilities

            for x in range(random.randint(0, len(factors))):  # for loop for the amount of items in Vulnerability list
                tmpVuln.add(factors[random.randint(0, (len(factors) - 1))])  # Adds random Vulnerability to set

            ''' Removed the age in the element of the key is now within the name set '''
            # tmpVuln.add(random.randint(0, 100))  random age value assigned to beginning of set
            y = {tmpIndiv: tmpVuln}  # y = the name and info of individual\

            dictTMP.update(y)  # individual added
            if len(dictTMP) != lenbefore:
                break

    return dictTMP  # full dictionary returned


def WriteData2FIle():
    print("enter name of file")
    filename = input()
    with open((filename + ".txt"), 'w') as f:
        for key, value in Data.items():
            f.write('%s:%s\n' % (key, value))


if __name__ == '__main__':
    Data = None  # Ditctionary of individuals to be sorted
    IncVFactors = ['Smoking', 'Drinking',
                   'HealthIssue', 'TraveledAbroad',
                   'EssentialWorker']  # List of factors which increase to Vulnerability of an individual
    ''' 
    IncVfactors is a lsit which contains the factors which increase the vulnerability of an individual    
    [ 'Smoking' , 'Drinking' , ' HealthIssue ' ]
    Individuals Contain a name , age , ID number and factors relating to their vulnerability to COVID
    final dict will look as such:
    {  (name, age, ID number):{ Vulnerabilities } 

    '''
    amount = int(input("please enter set amount"))
    Data = GenerateDataSet(amount, IncVFactors)
    print(Data)
    print("would you like to write the generated data to a file? (y/n)")
    if input() == 'y' or 'Y':
        WriteData2FIle()
