def switch():
    while True: 
        choice = int(input("Enter your choice: "))
        a = float(input("Enter a value: "))
        b = float(input("Enter b value: "))
        print("Select operation!")
        print("1. Addition")
        print("2. Subraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("X. Close")
        def add():
            result = a+b;
            print("a :",a,"\nb :",b,"\nresult: "+str(result))
    
        def sub():
            result = a-b;
            print("a :",a,"\nb :",b,"\nresult: "+str(result));

        def mul():
            result = a*b;
            print("a :",a,"\nb :",b,"\nresult: "+str(result));

        def div():
            result = a/b;
            print("a :",a,"\nb :",b,"\nresult: "+str(result));
        
        def mod():
            result = a%b;
            print("a :",a,"\nb :",b,"\nresult: "+str(result));

        def default():
            print("Invalid")
        
        if choice == 0:
            break;

        # Dictionary Mapping
        dict = {
            1 : add,
            2 : sub,
            3 : mul,
            4 : div,
            5 : mod,
        }
        dict.get(choice,default)()

switch()
    
    
    


