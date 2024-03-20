import json

# 1: json - dump, load <-- file을 읽어올 때
# 2: json - dumps, loads <-- fast API, Flask// 일반적인 상황에서 많이 사용

# 방법 2번으로 진행 예시

data = {"name" : "Kim", "age":23}

print(data["name"], type(data))
print(json.dumps(data), type(json.dumps(data))) #딕셔너리를 str타입으로 변환
print(json.loads(json.dumps(data)),type(json.loads(json.dumps(data)))) #str 타입을 다시 변환