import random


def GenerateDataSet(n, factors):
    dictTMP = {}  # declaring a temporary dictionary
    Names = []  # list of available names
    Namefile = open('Names.txt', 'r')  # opening the Name file
    # For loop generates a list of names with no new line char
    for l in Namefile:
        Names.append(l.strip('\n'))

    # for loop which repeats N times meaning Lenth(DataDict) = N
    for i in range(n):
        tmpIndiv = Names[random.randint(0, len(Names))]  # selects random name and assigns to var
        tmpVuln = {''}  # declares a set which will contain Vulnerabilities
        for x in range(random.randint(0, len(factors))):  # for loop for the amount of items in Vulnerability list
            tmpVuln.add(factors[random.randint(0, (len(factors) - 1))])  # Adds random Vulnerability to set
        tmpVuln.discard('')
        tmpVuln.add(random.randint(0, 100))  # random age value assigned to begining of set
        y = {tmpIndiv: tmpVuln}  # y = the name and info of individual
        dictTMP.update(y)  # individual added
    return dictTMP  # full dictionary returned



if __name__ == '__main__':
    Data = None  # Ditctionary of individuals to be sorted
    IncVFactors = ['Smoking', 'Drinking',
                   'HealthIssue']  # List of factors which increase to Vaunerability of an individual
    ''' 
    IncVfactors is a lsit which contains the factors which increase the vulnerability of an individual    
    [ 'Smoking' , 'Drinking' , ' HealthIssue ' ]
    Individuals Contain a name and factors relating to their vulnerability to COVID
    THE AGE WILL ALWAYS BE THE FIRST VALUE
    {  'Marceli' : { 18 , Smoking } , 'Name' : { Age , Issues... }}
        
    '''
    Data = GenerateDataSet(10, IncVFactors)
    print(Data)
