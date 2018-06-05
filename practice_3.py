def choice_to_number(string):
    return { 'usain': '1','me': '2','himanshu': '3'}[string]

def number_to_choice(number):
    return {1: 'usain', 2: 'me', 3: 'himanshu'}[number]

user_input = str(input('Enter the name for the position \n1.usain\n2.me\n3.himanshu\n\n'))

print('The position is', choice_to_number(user_input))

def test_choice_to_number():
    assert choice_to_number('usain') == '1'
    print("\n your code is correct")
def test_number_to_choice():
    assert number_to_choice(1) == 'usain'
    print("\n your code is correct")
    
test_choice_to_number()
test_number_to_choice()