pi=3.14

def oneHapN(end):
    sum=0
    for i in range(end):
        sum += i+1
    return sum

def oneGopN(end):
    total = 1
    for i in range(end):
        total *= i+1
    return total

def twoHanN(start,end):
    sum=0
    for i in range(start,end+1):
        sum+=i
    return sum

def twoGopN(start,end):
    total=1
    for i in range(start,end+1):
        total*=i
    return total