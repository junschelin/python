import json

data = '{"name" : "Kim", "age":23}'
member = {"name" : "Lee", "age": 24}


# with open('member2.json', 'r') as r_file:
#     d = json.load(r_file)
#     print(d, type(d))
    
d2 = json.dumps(member)
print(d2, type(d2))

d3 = json.loads(d2)
print(d3, type(d3), d3["name"])