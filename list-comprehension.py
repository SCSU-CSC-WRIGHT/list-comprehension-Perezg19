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
    num_of_int=int(input("Please enter how many numbers you will be entering: "))
    oddl=[]
    evenl=[]
    for i in range(num_of_int):
        int_input=(input(f"Please enter your numbers for your lists, and seperate with spaces: "))
        for i in int_input.split():
            i=(int(i))
            if i % 2 == 0:
                oddl.append (i)
            else:
                evenl.append (i)
        print("\nOdd numbers: ", oddl)
        print("Even numbers: ", evenl)
#lab_2()

def lab_3():
    list_1= []
    list_2= []
    ask_input1=(input("Please enter numbers for list 1, seperated with spaces: "))
    for i in ask_input1.split():
        list_1.append(int(i))
    ask_input2=(input("Please enter numbers for list 2, seperated with spaces: "))
    for i in ask_input2.split():
        list_2.append(int(i))
    print("Here are your lists:",list_1, list_2)
    print("Now watch as I remove all your duplicates, ")
    list_3=list_1+list_2
    for number in list_1:
        if number in list_2:
            list_3.remove(number)
    print("Here is your merged list with no duplicate numbers! ", list_3)
lab_3()