'''
user_input = str(input('Enter the string : \n'))
print("The length of the string is ", len(user_input))


def string_length(string):
    count =0
    for i in string:
        count += 1
    return count


user_string = str(input('Enter the string: '))
print('The length of the string is ', string_length(user_string))

def last_letter(string):
    return string[-1]
user_string = str(input('Enter the string: '))
print('The last letter of the string is ', last_letter(user_string))
'''
def greater_than(num1, num2, num3):
    return max(num1, num2, num3)

input_1, input_2, input_3 = int(input('Enter the first number: ')), int(input('\nEnter the second number: ')), int(input('\nEnter the third number: '))
print("The bigger number is", greater_than(input_1, input_2, input_3))

def test_greater_than():
    print('--------RUNNING TEST-------')
    assert greater_than(1,2,3) == 3
    print("\n YOUR CODE IS CORRECT")

test_greater_than()
    