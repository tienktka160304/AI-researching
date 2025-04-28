users = {'tien' : 'active', 'hiein' : 'inactive', 'as' : 'active'}

for user, status in users.copy().items():
    if status == "inactive":
        del users[user]
        
active_user = {}
for user, status in users.items():
    if status == 'active':
        active_user[user] = status
        
print(users,end= '\n')
print(active_user)
# {'tien': 'active', 'as': 'active'}
# {'tien': 'active', 'as': 'active'}