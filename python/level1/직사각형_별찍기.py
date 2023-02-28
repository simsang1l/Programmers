a, b = map(int, input().strip().split(' '))
# print(a + b)
print(('*' * a + '\n') * b)
    
## 다른사람 풀이
a, b = map(int, input().strip().split(' '))
# print(a + b)
for i in range(b):
    print('*' * a)