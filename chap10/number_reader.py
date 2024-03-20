from pathlib import Path
import json




# js에서 사용하는 문법
# data = json()
# print(type(data))
# data = json.parse("{'a':1, 'b':2}")
# print(data.a)
# print(data.b)

path = Path('numbers.json')
contents = path.read_text()
numbers = json.loads(contents)
print(numbers)