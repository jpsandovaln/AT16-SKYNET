import json

#json string data
employee_string = '{"first_name": "Michael", "last_name": "Rodgers", "department": "Marketing"}'

#check data type with type() method
#print(type(employee_string))

#convert string to  object
json_object = json.loads(employee_string)

#check new data type
print(type(json_object))