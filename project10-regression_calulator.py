def add(a,b):
    return a+b

def substraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    return a/b

operation = {"+":add, "-":substraction, "*":multiplication , "/":division}
num1 = int(input("please enter first number \t "))

for keys in operation:
    print(keys)
    
continue_operation = True
while continue_operation != False:   
    output_symbol = input("Please select the operation \t")
    num2 = int(input("please enter second number \t "))
    caluator_function = operation[output_symbol]
    output = caluator_function(num1,num2)
    print(output)

    next_operation = input(f"enter y to continue with {output} , n to exit \t").lower()
    if next_operation == 'y':
        num2 = int(input("please enter second number \t "))
    
    



