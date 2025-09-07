questions=[
    ["which is the last planet in our solar system?","mercury","venus","neptune","earth",3],
    ["which color is mars?","red","yellow","orange","white",1],
    ["which planet has a ring?","earth","venus","mars","saturn",4],
    ["which is the largest planet?","uranus","jupiter","neptune","earth",2],
    ["in which planet human live?","mercury","venus","earth","uranus",3]
    ]
prices=[1000,2000,3000,4000,5000]
i=0
for question in questions:
    print(f"{question[0]}")
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")
    
    a=int(input("Enter your choice 1 for a , 2 for b , 3 for c , 4 for d : "))
    if(question[5]==a):
        print("correct answer")
    else:
        print(f"incorrect, correct answer is {question[5]}")
        print("better luck next time ")
        break
    print(f"you won {prices[i]}")
    i+=1