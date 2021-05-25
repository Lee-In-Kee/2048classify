import random

MAX_LENGTH = 4
CELL_EMPTY = '□'
row = [[CELL_EMPTY for _ in range(MAX_LENGTH)] for i in range(MAX_LENGTH)]
column = [[CELL_EMPTY for _ in range(MAX_LENGTH)] for i in range(MAX_LENGTH)]
rn = [0, 0]

def function_Row(idx, vector_x):
    # 좌or우로 밀착
    for i in range(MAX_LENGTH):
        num = row[i].count(CELL_EMPTY)
        cnt = 0
        while cnt < num:
            cnt += 1
            row[i].remove(CELL_EMPTY)
        cnt = 0
        while cnt < num:
            cnt += 1
            row[i].insert(idx,CELL_EMPTY)

    # 같은 값끼리 합침
    for i in range(MAX_LENGTH):
        cnt = 0
        while cnt < MAX_LENGTH - 1:
            if row[i][MAX_LENGTH-1-idx+cnt*vector_x] == row[i][MAX_LENGTH-1-idx+(cnt+1)*vector_x] and row[i][MAX_LENGTH-1-idx+cnt*vector_x] != CELL_EMPTY:
                row[i][MAX_LENGTH-1-idx+cnt*vector_x] = str(int(row[i][MAX_LENGTH-1-idx+cnt*vector_x]) * 2)
                row[i][MAX_LENGTH-1-idx+(cnt+1)*vector_x] = CELL_EMPTY
            cnt += 1

    # 좌or우로 밀착
    for i in range(MAX_LENGTH):
        num = row[i].count(CELL_EMPTY)
        cnt = 0
        while cnt < num:
            cnt += 1
            row[i].remove(CELL_EMPTY)
        cnt = 0
        while cnt < num:
            cnt += 1
            row[i].insert(idx,CELL_EMPTY)

def function_column(idx, vector_y):
    # 상or하로 밀착
    for i in range(MAX_LENGTH):
        num = column[i].count(CELL_EMPTY)
        cnt = 0
        while cnt < num:
            cnt += 1
            column[i].remove(CELL_EMPTY)
        cnt = 0
        while cnt < num:
            cnt += 1
            column[i].insert(idx,CELL_EMPTY)

    # 같은 값끼리 합침
    for i in range(MAX_LENGTH):
        cnt = 0
        while cnt < MAX_LENGTH - 1:
            if column[i][MAX_LENGTH-1-idx+cnt*vector_y] == column[i][MAX_LENGTH-1-idx+(cnt+1)*vector_y] and column[i][MAX_LENGTH-1-idx+cnt*vector_y] != CELL_EMPTY:
                column[i][MAX_LENGTH-1-idx+cnt*vector_y] = str(int(column[i][MAX_LENGTH-1-idx+cnt*vector_y]) * 2)
                column[i][MAX_LENGTH-1-idx+(cnt+1)*vector_y] = CELL_EMPTY
            cnt += 1

    # 상or하로 밀착
    for i in range(MAX_LENGTH):
        num = column[i].count(CELL_EMPTY)
        cnt = 0
        while cnt < num:
            cnt += 1
            column[i].remove(CELL_EMPTY)
        cnt = 0
        while cnt < num:
            cnt += 1
            column[i].insert(idx,CELL_EMPTY)

    for i in range(MAX_LENGTH):
            for j in range(MAX_LENGTH):
                row[j][i] = column[i][j]

# 첫 시작
cnt = 0
while cnt < 2:
    cnt += 1
    rn[0] = random.randrange(0,4)
    rn[1] = random.randrange(0,4)
    while row[rn[0]][rn[1]] != CELL_EMPTY:
        rn[0] = random.randrange(0,4)
        rn[1] = random.randrange(0,4)

    row[rn[0]][rn[1]] = '2'

#첫 출력
for i in range(MAX_LENGTH):
    print(' '.join(row[i]))

# 반복
total = 0
while total < 100:
    total += 1
    # column 데이터 수집
    for i in range(MAX_LENGTH):
        for j in range(MAX_LENGTH):
            column[j][i] = row[i][j]

    # 입력(w,a,s,d)
    in_Value = ['w', 's', 'a', 'd']
    while True:
        shift = input('방향키 입력: ')
        if shift in in_Value:
            break

    if shift == 'd':
        idx = 0
        vector_x = -1
        function_Row(idx,vector_x)
   
    if shift == 'a':
        idx = MAX_LENGTH - 1
        vector_x = 1
        function_Row(idx,vector_x)

    if shift == 'w':
        idx = MAX_LENGTH - 1
        vector_y = 1
        function_column(idx,vector_y)

    if shift == 's':
        idx = 0
        vector_y = -1
        function_column(idx,vector_y)

    # 실패조건
    cnt = 0
    for i in range(MAX_LENGTH):
        if CELL_EMPTY in row[i]:
            cnt += 1
    if cnt == 0:
        break

    # 랜덤 위치에 '2'생성
    rn[0] = random.randrange(0,4)
    rn[1] = random.randrange(0,4)
    while row[rn[0]][rn[1]] != CELL_EMPTY:
        rn[0] = random.randrange(0,4)
        rn[1] = random.randrange(0,4)

    row[rn[0]][rn[1]] = '2'

    # 열 맞춤
    visual = [['0'for _ in range(MAX_LENGTH)] for i in range(MAX_LENGTH)]
    maxL = []
    for i in range(MAX_LENGTH):
        for j in range(MAX_LENGTH):
            visual[j][i] = len(row[i][j])
    for j in range(MAX_LENGTH):
        maxL.append(max(visual[j]))

    for i in range(MAX_LENGTH):
        for j in range(MAX_LENGTH):
            visual[i][j] = row[i][j].rjust(maxL[j],' ')


    #최종 출력
    for i in range(MAX_LENGTH):
        print(' '.join(visual[i]))
