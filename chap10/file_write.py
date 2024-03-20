from pathlib import Path
path = Path ('./chap10/aaa/aaa.txt')
if path.exist():
    with open(path, 'w') as file:
        file.write('a\n')
        file.write('aa\n')
        file.write('aaa')
        
try:
    if path.exist():
        with open(path, 'w') as file:
            file.write('a\n')
            file.write('aa\n')
            file.write('aaa')
except Exception as e:
    pass
    print(e)
    
