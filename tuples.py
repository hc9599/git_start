groceries =('banana', 'mango', 'apple',1,2)

aadhar_no = ('12345', '65743', '87690') #never wanted to change that is tuples


#mutable datatype are the type which can be changed #immutable datatype are the type which can not be changed 
groceries_with_aadhar_no = groceries + aadhar_no

print(groceries_with_aadhar_no)
print(groceries*4)
print(type(groceries*4))
print("".join(aadhar_no))