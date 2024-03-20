import sys

def cantore(squared, lines, start=0):
    if squared == 0:
        return
    
    third = 3 ** (squared - 1)
    
    for i in range(third):
        lines[start + third + i] = ' '
    cantore(squared - 1, lines, start)
    cantore(squared - 1, lines, start + 2 * third)

while True:
    try:    
        input = sys.stdin.readline

        n = int(input().rstrip())
        lines = ['-'] * 3 ** n
        cantore(n, lines)
        print(''.join(lines))
    except:
        pass