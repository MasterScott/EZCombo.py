ComboList = []
ComboIterator = 0
Username = ''
Password = ''
Combo = ''
GoodCombos = []

def LoadCombos(ComboPath):
    global ComboList
    global ComboIterator
    try:
        Combos = open(ComboPath,'r')
        for line in Combos:
            strippedcombo = line.replace('\n','')
            ComboList.append(strippedcombo)
            ComboIterator+=1
        return ComboList
        return ComboIterator
    except IOError:
        print('Could Not Find ComboList. Is the Path Correct?')

def PullCombo(ComboIterator):
    global Username
    global Password
    global ComboList
    try:
        Username,Password = ComboList[ComboIterator].split(':',1)
        return Username
        return Password
    except:
        print('Error Parsing Combo. Is it in proper Format? (Username:Password) Maybe you forgot to call LoadCombos() first')

def RemoveCombo(Combo):
    global ComboList
    try:
        ComboList.remove(Combo)
        return ComboList
    except:
        print('Error Removing Combo, is it in proper format? (Username:Password)')

def SaveValids(SaveName):
    global GoodCombos
    try:
        ValidFile = open(SaveName,'a')
        for line in GoodCombos:
            ValidFile.write(line + "\n")
        return GoodCombos
    except:
        print('Error Saving Good Combos!')
