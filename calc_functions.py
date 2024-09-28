# addition
def do_addition(a:int,b:int):
    return a+b
#subtraction
def do_subtraction(a:int,b:int):
    return a-b

def do_multiplication(a,b):
    return a*b

def do_division(a,b):
    try:
        return a/b
    except ZeroDivisionError as e :
        return "Cannot divide by Zero!"
    
def calculate_area_rectangle(a,b):
    return a*b

