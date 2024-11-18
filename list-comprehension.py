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
        int_input=(input(f"Please enter your numbers for list {i+1}, and seperate with spaces: "))
        numbers = int_input.split()
        for nums in numbers:
            num=int(nums)
        if num % 2 == 0:
            oddl.append (num)
        else:
            evenl.append (num)
        print("\nOdd numbers: ", oddl)
        print("Even numbers: ", evenl)
lab_2()
