row, col = map(int, input().split())

m_A = []
m_B = []
m_add = []
m_C = []

for i in range(row*2):
    if i < row:
        m_A.append(list(map(int, input().split())))
    else:
        m_B.append(list(map(int, input().split())))

for i in range(row):
    for j in range(col):
        m_add.append((m_A[i][j] + m_B[i][j]))
    m_C.append(m_add)
    m_add = []

for i in range(row):
    for j in range(col):
        print(m_C[i][j], end = ' ')