while True: 
    multiplication_no = int(input("Enter the number for which you want multiplication table: "))
    end_no = int(input("Enter the number till where you want the multiplication: "))
    for i in range(1,end_no+1):
        print(multiplication_no,'X',i,'=',multiplication_no * i)
    
    continue_choice = str(input("want to continue(y/n): "))
    if continue_choice == 'n':
        break