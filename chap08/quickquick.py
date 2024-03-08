def modify_string(s): # String 값을 전달 받았음
    ### immutable 변수는 튜플, 숫자, String, Boolean 
    s = s+ 'world' # String s 는 원래 변수가 가리키는 주소랑 다르다.
    print(s)

st = "hello "
modify_string(st)
print(st) ##출력 결과가 hello => immutable


