a = int(input())
if a % 2 == 0 :
    print(a, 'is even')
else :
    print(a, 'is odd')


# 다른사람 풀이
n=int(input())
print(f"{n} is {'eovdedn'[n&1::2]}")

N = int(input())
print(f"{N} is {'even' if N % 2 == 0 else 'odd'}")