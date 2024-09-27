from calc_functions import do_addition, do_subtraction



def main():
    print('Welcome to the calculator app')
    print("""select the function from the given options:
          0.Add
          1.Subtract
          """)
    user_input=input("select the option:")
    a=int(input('Value of A:'))
    b=int(input('Value of B:'))


    if user_input=="0":
        result=do_addition(a,b)
        print(result)
        
    else:
        result1=do_subtraction(a,b)
        print(result1)

    

        
        
        
# this is the main file 
if __name__=="__main__":
    main()

    
    
