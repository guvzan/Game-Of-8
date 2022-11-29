import copy

posJournal=[]
endState=[]
logState=[]
buffer=[[1, 7, 0],                              #Початковий стан
        [3, 4 ,8],
        [2, 6, 5]]
posJournal.append(buffer)
buffer=[[1, 2, 3],                              #Кінцевий стан
        [4, 5 ,6],
        [7, 8, 0]]
endState.append(buffer)
buffer=[]
logJournal=[0]

def countMisposition(array, endArray):          #Функція, що повертає кількість фішок не на своїх місцях
    counter=0
    for i in range(0, 3):
        for j in range(0, 3):
            if(array[i][j]!=endArray[i][j]):
                counter+=1
    return(counter)

def countManhattan(array, endArray):            #Функція, що повертає значення манхеттенської відстані
    distance = 0
    for i in range(0, 3):
        for j in range(0, 3):
            for k in range(0, 3):
                for l in range(0, 3):
                    if(endArray[k][l]==array[i][j]):
                        distance+=abs(i-k)+abs(j-l)
    return(distance)

def printTable(array):                          #Функція, що виводить заданий стан
    for i in range(0, 3):
        print(array[i], sep='\n')

def findZero(array):                            #Функція, що повертає координати порожньої фішки
    for i in range(0, 3):
        if(array[i].count(0)==1):
            return(i, array[i].index(0))

def move(array, direction):                     #Функція, що повертає новоутворений стан
    copyOfArray=array
    row, col=findZero(copyOfArray)
    if(direction=="left" and col>0):
        copyOfArray[row][col], copyOfArray[row][col-1]=copyOfArray[row][col-1], copyOfArray[row][col]
        return (copyOfArray)
    elif (direction == "up" and row > 0):
        copyOfArray[row][col], copyOfArray[row-1][col] = copyOfArray[row-1][col], copyOfArray[row][col]
        return (copyOfArray)
    elif (direction == "right" and col <2):
        copyOfArray[row][col], copyOfArray[row][col + 1] = copyOfArray[row][col + 1], copyOfArray[row][col]
        return (copyOfArray)
    elif (direction == "down" and row<2):
        copyOfArray[row][col], copyOfArray[row+1][col] = copyOfArray[row+1][col], copyOfArray[row][col]
        return (copyOfArray)


print("Початковий стан")
printTable(posJournal[0])
print()
print("Кінцевий стан")
printTable(endState[0])
print("Натисніть Enter щоб почати генерацію станів")
print()
print("\"Enter\" to see next state\n\"S\" to skip to the solution")



pointer=0
journalLength=1
stateCounter=1
moves=["left", "up", "right", "down"]
distances=[999, 999, 999 ,999]
show=True
skip=False
try:
    while(posJournal[-1]!=endState[0]):             #Цикл, що виконується доки не буде знайдено результат
        if(skip==False):
            value=input()
            if(value=="S"):
                skip = True
                show = False
            else:
                pass


        distances=[999, 999, 999 ,999]




        journalCopy=copy.deepcopy(posJournal[pointer])          #Спроба руху вліво
        temp=move(journalCopy, "left")
        if(temp!=None):
            stateCounter += 1
            if(posJournal.count(temp) == 0):
                distances[0]=countMisposition(temp, endState[0])+countManhattan(temp, endState[0]) #Значення оціночної функції


        journalCopy = copy.deepcopy(posJournal[pointer])        #Спроба руху вверх
        temp = move(journalCopy, "up")
        if (temp != None):
            stateCounter += 1
            if (posJournal.count(temp) == 0):
                distances[1] = countMisposition(temp, endState[0])+countManhattan(temp, endState[0]) #Значення оціночної функції


        journalCopy = copy.deepcopy(posJournal[pointer])        #Спроба руху вправо
        temp = move(journalCopy, "right")
        if (temp != None):
            stateCounter += 1
            if (posJournal.count(temp) == 0):
                distances[2] = countMisposition(temp, endState[0])+countManhattan(temp, endState[0]) #Значення оціночної функції


        journalCopy = copy.deepcopy(posJournal[pointer])        #Спроба руху вниз
        temp = move(journalCopy, "down")
        if (temp != None):
            stateCounter += 1
            if (posJournal.count(temp) == 0):
                distances[3] = countMisposition(temp, endState[0])+countManhattan(temp, endState[0]) #Значення оціночної функції

        minimum=min(distances)
        if(minimum<=500):       #Визначення та запис найкращого ходу
            for i in range(0, 4):
                if(distances[i]==minimum):
                    journalCopy = copy.deepcopy(posJournal[pointer])
                    temp=move(journalCopy, moves[i])
                    posJournal.append(temp)
                    logJournal.append(pointer)
                    journalLength += 1
                    if(show==True):
                        print("\nState ", pointer + 1, "to state ", journalLength, "Moving ", moves[i])
                        print("h=", minimum)
                        printTable(temp)




        pointer+=1
except IndexError:
    print("Рішення не існує")
    exit()



print("\nEnd State Achieved!")
printTable(posJournal[-1])

print("\nПослідовність переходів для досягнення заданого кінцевого стану:\n")

index2=-1
for i in posJournal:            #Вивід ходів від першого стану до кінцевого

    previous=logJournal[index2]
    bufferState=posJournal[previous]
    logState.append(bufferState)
    for k in range(0, journalLength):
        if(bufferState==posJournal[k]):
            index2=k
            break
    if(bufferState==posJournal[0]):
        break


counter=0
logState.reverse()
for i in logState:
    printTable(i)
    print()
    counter+=1
printTable(endState[0])

print("\nГлибина дерева: ", counter+1)              #Інформація про утворене дерево ходів
print("Загальна кільксть згенерованих станів: ", stateCounter)
print("Кількість станів, занесених в базу станів: ", journalLength)
print("Кількість відкинутих станів: ", stateCounter-journalLength)

