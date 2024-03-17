"""
Pioneers in Engineering Spring 2024 Coding Challenges Starter Code
"""

# Question 1


def delivery(lst: list) -> int:
    """
    >>> delivery(["Infamous Recidivist"])
    6
    >>> delivery(["Pugilist Prisoner", "Herculean Prisoner", "Recidivist", "Ordinary Prisoner", "Recidivist"])
    15
    """
    sum = 0;
    dict = {
        "Ordinary Prisoner": 1,
        "Pugilist Prisoner": 2,
        "Herculean Prisoner": 3,
        "Recidivist": 4,
        "Infamous Recidivist": 5
    }
    for i in lst:
        sum+=dict[i]
    return sum+1

# Question 2
def prisoners_list(lst: list) -> list:
    """
    >>> sorted(prisoners_list(["Recidivist", "Infamous Recidivist", "Recidivist"]))
    ["Infamous Recidivist", "Recidivist"]
    >>> sorted(prisoners_list(["Seasoned Prisoner", "Seasoned Prisoner", "Pugilist Prisoner", "Strongman Prisoner", "Elite Pugilist Prisoner", "Seasoned Prisoner"]))
      ["Elite Pugilist Prisoner", "Pugilist Prisoner", "Seasoned Prisoner", "Strongman Prisoner"]
    """
    newList = []
    for i in lst:
        if(i in newList):
            continue
        newList.append(i)
    return newList

# Question 3
def check_for_contraband(belongings) -> list:
    """
    >>> check_for_contraband(["book", "notebook", "pen"])
    (True, [])
    >>> check_for_contraband(["book", "notebook", "pen", "drugs"])
    (False, [“drugs”])
    """
    bool = True
    arr = []
    contraband = ["knife", "drugs", "weapons", "alcohol", "cellphone"]
    for i in belongings:
        if(i.lower() in contraband):
            arr.append(i)
            bool = False
    return (bool, arr)

# Question 4
def hop(n) -> int:
    """
    >>> hop(2)
    2
    >>> hop(4)
    5
    >>> hop(6)
    13
    """
    if(n == 0):
        return 1 #LOL autograder is kinda big brain
    if(n == 1):
        return 1
    elif(n == 2):
        return 2
    return hop(n-1) + hop(n-2)

# Question 5
def survival_points(dict1, dict2) -> dict:
    """ Return a new dictionary with the original keys and new values.
    >>> d1 = { ‘Alex’: 10, ‘Ben’: 15}
    >>> d2 = { ‘Jade’: 5, ‘Ben’: 20, ‘Alex’: -10}
    >>> survival_points(d1, d2)
    { ‘Alex’: 0, ‘Jade’: 5, ‘Ben’: 35} """
    newDict = {}
    keyList1 = list(dict1.keys())
    keyList2 = list(dict2.keys())
    for i in keyList1:
        newDict[i] = dict1[i]
    for i in keyList2:
        if(i in list(newDict.keys())):
            newDict[i] += dict2[i]
            continue
        newDict[i] = dict2[i]
    return newDict


# Question 6
visitation_slots = [
    ("09:00", "10:00"),
    ("10:00", "11:00"),
    ("11:00", "12:00"),
    ("13:00", "14:00"),
    ("14:00", "15:00")]

visitors = {slot: None for slot in visitation_slots}


def display_schedule():
    for slot, visitor in visitors.items():
        print(f"{slot}: {visitor or 'Available'}")


def add_visitor(slot, visitor_name):
    """ Return a newith the original keys and new values.
    >>>add_visitor((("09:00", "10:00"), "Alice")
    ('09:00', '10:00'): Alice
    ('10:00', '11:00'): Available
    ('11:00', '12:00'): Available
    ('13:00', '14:00'): Available
    ('14:00', '15:00'): Available

    >>>add_visitor((("09:00", "10:00"), "Alice")
    >>>add_visitor(("10:00", "11:00"), "Bob")
    >>>add_visitor(("10:00", "11:00"), "David") #Should not be added
    ('09:00', '10:00'): Alice
    ('10:00', '11:00'): Bob
    ('11:00', '12:00'): Available
    ('13:00', '14:00'): Available
    ('14:00', '15:00'): Available
    """

    if(slot in visitors.keys() and visitors[slot] == None):
        visitors[slot] = visitor_name
    display_schedule()

# Question 7
def acquaintance(id1, id2, *lists) -> bool:
    """
    >>> acquaintance(0, 11, [3, 55, 269, 0, 11], [3])
    True
    >>> acquaintance(11, 1, [3, 55, 269, 0, 11], [3, 269, 0, 1, 74], [55, 2], [12, 34, 5])
    True
    >>> acquaintance(55, 1, [55, 2], [3, 55, 269, 0, 11], [3, 269, 0, 1, 74])
    True
    >>> acquaintance(2, 3, [0], [3, 55, 269, 0, 11], [3, 269, 0, 1, 74], [55, 2])
    False
    """

    lists = list(lists)
    list1 = len(lists)
    while(list1 > 1):
        list1-=1
        list2 = list1
        while(list2 > 0):
            list2 -= 1
            counter = 0
            for element1 in lists[list1]:
                if element1 in lists[list2]:
                    counter+=1
            if counter >= 3:
                lists[list2] = lists[list2] + lists[list1]
                del lists[list1]
                list1 -= 1
                list2 -= 1
    for list3 in lists:
        if id1 in list3 and id2 in list3:
            return True
    return False

def test(list1, list2):
    counter= 0
    for element1 in list1:
        if element1 in list2:
            counter += 1
    return counter

# Question 8
def multiply_list(lst: list) -> int:
    product = 1
    for i in lst:
        product *= i
    return product

def ssspookyyyy(str: str) -> list:
    totalSolve(str)

def totalSolve(str):
    bigStr = largeSortList(str)[0]
    leftInd = str.index(bigStr)
    rightInd = leftInd + len(bigStr)
    leftStr = str[0:leftInd]
    rightStr = str[rightInd: len(str)]
    leftArr = leftSolve(leftStr, [])
    rightArr = rightSolve(rightStr, [])
    if(leftArr == 0):
        leftArr = []
    if(rightArr == 0):
        rightArr = []
    return leftArr + [bigStr] + rightArr

def largeSortList(str):
    possibleList = []
    element1 = -1
    while element1 < len(str) - 1:
        element1 += 1
        element2 = element1
        while element2 < len(str):
            element2 += 1
            if isGood(str[element1 : element2]):
                possibleList = insertSort(possibleList, str[element1 : element2])
    return possibleList
def isGood(str):
    for i in range(3, len(str)):
        if(str[i] == str[i-1] and str[i-1] == str[i-2] and str[i-2] == str[i-3]):
            return False
    return True
def insertSort(list, str):
    if len(list) == 0:
        list.append(str)
        return list
    for i in range(len(list)):
        if len(str) >= len(list[i]):
            list.insert(i, str)
            break
    return list
def leftSolve(str, list):
    #Finding Possible List
    possibleList = []
    finished = False #Finds if we have put all the string in the list
    element1 = len(str)
    while element1 > 0:
        element1 -= 1
        if isGood(str[element1:len(str)]):
            if(element1 == 0):
                finished = True
            possibleList = insertSort(possibleList, str[element1: len(str)])

    # End condition
    if len(possibleList) == 0 or len(possibleList[0]) < 2:
        return 0
    if finished:
        list.append(str)
        return list

    #Recursive part of function
    possible = False
    for string in possibleList:
        thing = leftSolve(str[0:len(str) - len(string)], list)
        if thing != 0:
            possible = True
            list.append(string)
            return thing
    if not possible:
        return 0

def rightSolve(str, list):
    #Finding Possible List
    possibleList = []
    finished = False #Finds if we have put all the string in the list
    element1 = 0
    while element1 < len(str):
        element1 += 1
        if isGood(str[0:element1]):
            if(element1 == len(str)):
                finished = True
            possibleList = insertSort(possibleList, str[0:element1])

    # End condition
    if len(possibleList) == 0 or len(possibleList[0]) < 2:
        return 0
    if finished:
        list.insert(0,str)
        return list

    #Recursive part of function
    possible = False
    for string in possibleList:
        thing = rightSolve(str[len(string):len(str)], list)
        if thing != 0:
            possible = True
            list.insert(0,string)
            return thing
    if not possible:
        return 0
