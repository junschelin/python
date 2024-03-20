# dic1 = {'정원' : 'A+'}
# dic2 = {'윤정' : 'A+'}
# dic3 = {'세영' : 'A+'}
# dic = {1:dic1, 2:dic2, 3:dic3}
# print(dic)

db = {
    1 : {'정원' : 'A+'},
    2 : {'윤정' : 'A+'}, 
    3 : {'세영' : 'A+'}
}

print(db)

db[4] = {'진수' : 'B0'}

if 4 in db:
	print(db.get(4))
    
print(db.get(5, 0)) #key 5가 있으면 가져오고 없으면 0을 가져와라

for k, v in db.items():
    print(k, v)

first = lambda x:x[0]
for row in db.items():
      print(first(row))

first = lambda x:x[1]
for row in db.items():
      print(first(row))