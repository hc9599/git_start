while True:
    mul_no = int(input('Enter the number you want to have multiplication number: '))
    range_no = int(input('Enter the number till you want multiplication: '))
    for i in range(1, range_no+1):
        print(mul_no, 'X', i, '=', mul_no*i)
    choice_op = str(input('Want to continue(y/n): '))

    if choice_op == 'n':
        break
    