ComboList = []
GoodCombos = []
BadCombos = []
TotalCombos = 0
ComboIterator = 0
Username = ''
Password = ''
Combo = ''

def LoadCombos(ComboPath):
    global ComboList
    global TotalCombos
    try:
        Combos = open(ComboPath,'r')
        for line in Combos:
            strippedcombo = line.replace('\n','')
            ComboList.append(strippedcombo)
            TotalCombos+=1
        return ComboList , TotalCombos
    except IOError:
        print('Could Not Find ComboList. Is the Path Correct?')

def PullCombo(ComboIterator):
    global Username
    global Password
    global ComboList
    try:
        Username,Password = ComboList[ComboIterator].split(':',1)
        return Username , Password
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
        ValidFile.close()
        return GoodCombos
    except:
        print('Error Saving Good Combos!')

def GoodCombo(capture , data):
    try:
        global Username
        global Password
        global GoodCombos
        GoodCombos.append(Username + ':' + Password + capture + data)
    except:
        print("Error Appending Combo. Did you pass Capture Name and Capture Data?")

def BadCombo():
    try:
        global Username
        global Password
        global BadCombos
        BadCombos.append(Username + ':' + Password)
    except:
        print("Error Appending Bad Combo")

def SaveFails(SaveName):
    global BadCombos
    try:
        BadFile = open(SaveName,'a')
        for line in BadCombos:
            BadFile.write(line + "\n")
        BadFile.close()
        return BadCombos
    except:
        print('Error Saving Bad Combos!')
