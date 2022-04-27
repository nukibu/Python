#------------------------------------------

# list = [1,2,3]
# double = [item * 2 for item in list]

# new_list = (x * 2 for x in list)
# for x in new_list:
#   print(x)

# for item in list:
#   double.append(item * 2)
#print(double)

#------------------------------------------

# users = [{'name': 'Manuel', 'age': 31}, {'name': 'Max', 'age': 30}, {'name': 'Dirk', 'age': 38}]

# user_name = [user['name'] for user in users if user['age'] > 30 and user['name'] == 'Dirk']
# print(user_name)

#------------------------------------------

user_groups = [
  [
    {'name': 'Manuel', 'age': 31},
    {'name': 'Max', 'age': 30}
  ],
  [
    {'name': 'Sarah', 'age': 29},
    {'name': 'Julie', 'age': 32}
  ]
]

user_names = [person['name'] for group in user_groups for person in group if person['age'] > 30]
print(user_names)
