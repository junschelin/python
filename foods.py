my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] # Deep Copy
print(my_foods)
my_foods.append('cannoli')
print(my_foods)
print(friend_foods)

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods # Shallow Copy
print(my_foods)
my_foods.append('cannoli')
print(my_foods)
print(friend_foods)

