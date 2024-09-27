from calc_functions import do_addition, do_subtraction, do_multiplication
from divide import do_division 
# from area import calculate_area_rectangle #> You can also import this line but for this you have to create area .py
from calc_functions import calculate_area_rectangle


def main():
    print('Welcome to the calculator app')
    print("""select the function from the given options:
          0.Add
          1.Subtract
          2. Multiply
          3.Divide
          """)
    user_input=input("select the option:")
    a=int(input('Value of A:'))
    b=int(input('Value of B:'))


    if user_input=="0":
        result=do_addition(a,b)
        print(result)
        
    elif user_input=="1":
        result1=do_subtraction(a,b)
        print(result1)

    elif user_input=="2":
        result2=do_multiplication(a,b)
        print(result2)
    
    elif user_input=="3":
        result3=do_division(a,b)
        print(result3) 

    else:
        result4=calculate_area_rectangle(a,b)
        print('Area is :',result4)
        
        
        
        
# this is the main file 
if __name__=="__main__":
    main()

    
    
