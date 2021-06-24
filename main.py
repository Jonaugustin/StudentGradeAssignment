import random
grades = []
menu = """
Main Menu
1. Display All Grades
2. Randomize Grades
3. Stats
4. Count Honours
5. Remove Failing
6. Exit
"""

def displayGrades():
    for x in grades:
        print(x)
    callInput()

def randGrades():
    global grades
    for i in range(len(grades)):
        grades[i] = random.randint(0, 100)
    callInput()

def stats():
    grades.sort()
    txt = """
    Lowest Grade: {}
    Highest Grade: {}
    Average Grade: {}
    """
    lowest = grades[0]
    highest = grades[len(grades)-1]
    totalmark = 0
    for i in range(len(grades)):
        totalmark += grades[i]
        average = totalmark/len(grades)
    print(txt.format(lowest, highest, average))
    callInput()

def countHonour():
    count = 0 
    for x in grades:
        if x > 80:
            count += 1
    print(count)
    callInput()

def removeFail():
    global grades
    newgrades = [x for x in grades if x > 50]
    grades = newgrades
    callInput()

def callInput():
    print(menu)
    option = int(input("Please select a number from 1 to 6: "))
    if option == 1:
        displayGrades()
    elif option == 2:
        randGrades()
    elif option == 3:
        stats()
    elif option == 4:
        countHonour()
    elif option == 5:
        removeFail()
    elif option == 6:
        exit()
    else: 
        option = int(input("Please select a number again from 1 to 6: "))
        
for i in range(50):
    grades.append(random.randint(0, 100))

callInput()

