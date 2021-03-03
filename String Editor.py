
def a():
    while True:
        line = input("Add a line: ")
        if line != '#':
            linelist.append(line)
            continue
        if line == '#':
            for numbers in range(0, len(linelist)):
                print(str(int(numbers+1)) + str('.'), linelist[numbers])
            break
            
def d():
    delline = int(input("Delete a line: "))
    del linelist[delline]
    for numbers in range(0, len(linelist)):
        print(str(int(numbers+1)) + str('.'), linelist[numbers])
            

def r():
    number = int(input("Replace line number: "))+1
    replacement = input("Replacement string: ")
    linelist.insert(number2,replacement)
    linelist.pop(number2)
    for numbers in range(0, len(linelist)):
        print(str(int(numbers+1)) + str('.'), linelist[numbers])
            

def f():
    str1 = input("Find string: ")
    newstr = input("Replace with: ")
    str1.replace([str1],newstr)
    linelist.insert(str1,newstr)
    linelist.pop(str1)
    for numbers in range(0, len(linelist)):
        print(str(int(numbers+1)) + str('.'), linelist[numbers])

def p():
    startone = int(input("Start line number: "))-1
    endone = int(input("End line number: "))
    starttwo = int(input("Start line number: "))-1
    endtwo = int(input("End line number: "))
    start1 = linelist[startone:endone]
    start2 = linelist[starttwo:endtwo]
    newlines = start1 + start2
    newlines = ' '.join(newlines)
    linelist.append(newlines)
    for numbers in range(0, len(linelist)):
        print(str(int(numbers+1)) + str('.'), linelist[numbers])
            

def c():
    linelist.clear()
    for numbers in range(0, len(linelist)):
        print(str(int(numbers+1)) + str('.'), linelist[numbers])
    

    
k = 0
linelist = []

while k == 0:
    command = input("Command a, d, r, f, p, c, q: ")
    if command == 'a':
        a()
    if command == 'd':
        d()
    if command == 'r':
        r()
    if command == 'f':
        f()
    if command == 'p':
        p()
    if command == 'c':
        c()
    if command == 'q':
        break
    continue
