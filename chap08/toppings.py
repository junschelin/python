# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print("Sorry, we are out of green peppers right now.")
#     else:
#         print(f"Adding {requested_topping}.")

# print("\Finished making your pizza!")


# requested_toppings = [] 

# if requested_toppings: # list 요소가 없으므로 false (요소 하나라도 있으면 true)
#     for requested_topping in requested_toppings:
#         print(f"Adding {requested_topping}.")
#     print("\Finished making your pizza!")
# else:
#     print("Are you sure you want a plain pizza?")

        
available_toppings = ['mushrooms', 'olives', 'green peppers', 
                      'peperoni', 'pineapple', 'extra cheese'] 

requested_toppings = ['mushrooms', 'french fires', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\Finished making your pizza!")



