from calc_functions import do_addition, do_subtraction
from calc_functions import do_division     
from area import calculate_area_rectangle

def main():
    print('Welcome to the calculator app')
    print("""select the function from the given options:
          0.Add
          1.Subtract
          3. Division
          3.Area
          """)
    user_input=input("select the option:")
    a=int(input('Value of A:'))
    b=int(input('Value of B:'))


    if user_input=="0":
        result=do_addition(a,b)
        print(result)
    
    elif user_input=="3":
        result=do_division(a,b)
        print(result)
        
    elif user_input =="3":
        result=calculate_area_rectangle(a,b)
        print(result)
        
        
    else:
        result1=do_subtraction(a,b)
        print(result1)

    

        
        
        
# this is the main file 
if __name__=="__main__":
    main()

    
    
