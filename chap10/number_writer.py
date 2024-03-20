from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]

path = Path('numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)
#json.dumps() : 입력 인수를 json 형식으로 변환
#json.loads() : json 타입을 데이터로 읽어옴
    