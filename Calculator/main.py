try:
    a=int(input("Enter the value of a : "))
    b=int(input("Enter the value of b : "))
    print("Input the valid operator for operation \n" \
    "+ for sum\n" \
    "- for subtraction\n" \
    "* for multiplication\n" \
    "/ for division\n")
    o=input("Enter the operator : ")
    match o:
        case "+":
            print(f"sum of a and b is {a+b}")
        case "-":
            print(f"subtration of a and b is {a-b}")
        case "*":
            print(f"multiplication of a and b is {a*b}")
        case "/":
            print(f"division of a and b is {a/b}")
except Exception as e:
    print("Input valid value of a and b")