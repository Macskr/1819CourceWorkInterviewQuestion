import random


def GenerateDataSet(n, factors):
    dictTMP = {}
    Names = []
    Namefile = open('Names.txt', 'r')
    for l in Namefile:
        Names.append(l.strip('\n'))

    for i in range(n):
        tmpIndiv = Names[random.randint(0, len(Names))]
        tmpVuln = {''}
        for x in range(random.randint(0, len(factors))):
            tmpVuln.add(factors[random.randint(0, (len(factors) - 1))])
        tmpVuln.discard('')
        tmpVuln.add(random.randint(0, 100))
        y = {tmpIndiv: tmpVuln}
        dictTMP.update(y)
    return dictTMP


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
