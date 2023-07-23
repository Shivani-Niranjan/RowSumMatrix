'''
return the sum of each row

Input
[ [1,2,3,4]
  [5,6,7,8]
  [9,2,3,4] ]

Output
[10, 26, 18]
'''

row = int(input())
col = int(input())
matrix = [[int(input()) for x in range(col)] for y in range(row)]
result = []

for i in range(row):
    sum = 0
    for j in range(col):
        sum +=matrix[i][j]
    result.append(sum)

print(result)