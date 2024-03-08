bicycles = ['trek', 'cannodale', 'redline', 'specialized']
print(bicycles)

print("인덱스 첫번째 요소 : " + bicycles[0].title())
print(f"인덱스 마지막 요소 : {bicycles[-1]}")
print(f"인덱스 마지막 하나 전 요소 : {bicycles[-2]}")

motorcycles=['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles[-1] = 'kia'
motorcycles.append("GM")
motorcycles.insert(1,'Samcheonri')
del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
print(f"the last owned motor was a {popped_motorcycle}")

motorcycles_rev=['honda', 'ducati', 'yamaha', 'suzuki', 'ducati']
print(motorcycles_rev)

motorcycles_rev.remove('ducati')
print(motorcycles_rev)

too_expensive = 'ducati'
motorcycles_rev.remove(too_expensive)
print(motorcycles_rev)
print(f"\nA {too_expensive} is too expensive for me")

