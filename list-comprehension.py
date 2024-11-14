def lab_1():
    num=int(input("Enter the number of scores: "))
    scores=[]
    for i in range(num):
        score=int(input("Enter the score "))
        scores.append (score)
        sum(scores)/len(scores)
    avg = sum(scores)/len(scores)
    if avg>= 90:
        print("A")
    elif avg>= 80 and avg<= 90:
        print("B")
    elif avg>= 70 and avg<= 80:
        print("C")
    elif avg>= 60 and avg<= 70:
        print("D")
    elif avg<= 59:
        print("F")
    avg=sum(scores)/len(scores)
    if avg>=90:
        print("A")
    elif avg>= 80 and 90:
        print("B")
    print(scores)
#lab_1()

def lab_2():
    numask=int(input("How many numbers will you add? "))
    oddl=[]
    evenl=[]
    for i in range(numask):
        intask=int(input("Please enter various numbers: "))
        if i % 2 != 0:
            oddl.append (intask)
        if i % 2 == 0:
            evenl.append (intask)
        print(oddl)
        print(evenl)
lab_2()