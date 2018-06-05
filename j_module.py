
import json
employee_data ='''
{
"people":[
{
"name":'himanshu',
"email": ['aa@gmail.com', 'bb@gmail.com'],
"married" : false
},
{
"name": "choudhary",
"email": ['ee@gmail.com', 'ff@gmail.com'],
"married" : true
},
]
}
'''
data = json.loads(employee_data)

print(data)

