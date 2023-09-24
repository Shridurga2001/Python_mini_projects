def currency_conversion():
    print("Convert Indian rupee to dollars")
    
    dollars = eval(input("Enter dollars: "))
    rupees = convert_to_rupees(dollars)
    print(dollars,"dollars ","= ",rupees,"rupees.")

convert_to_rupees = lambda dollars: dollars * 83.1
currency_conversion()