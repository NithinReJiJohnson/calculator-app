from calc_functions import do_addition, do_subtraction, do_multiplication
from divide import do_division

def main():
    print('Welcome to the calculator app')
    print("""select the function from the given options:
          1.Add
          2.Subtract
          3. Divide
          """)
    user_input=input("select the option:")
    a=int(input('Value of A:'))
    b=int(input('Value of B:'))

    if user_input=="1":
        result=do_addition(a,b)
        print(result)
    elif user_input=="2":
        result1=do_subtraction(a,b)
        print(result1)

    elif user_input=="3":
        result2=do_division(a,b)
        print(result2) 

    else:
        result2=do_multiplication(a,b)
        print(result2)
        
        
        
        
# this is the main file 
if __name__=="__main__":
    main()

    
    
