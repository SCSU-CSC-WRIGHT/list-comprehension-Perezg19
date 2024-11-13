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
    avg=sum(scores)/len(scores) #(Do this outside of the for loop)
    if avg>=90:
        print("A")
    elif avg>= 80 and 90:
        print("B")
    print(scores)
lab_1()


#invoke function with lab_1

#def lab_2(): split.()

#def lab_3(): 
#numbers = [1,7,11,13]
#test = [1,2,4,7]
    #for num in numbers:
        #if num in test:
        #test.remove(num)
    #return numbers + test
    #check=input
    #if check=exit
        #break
    #Skip second bullet
    #Skip last bullet 