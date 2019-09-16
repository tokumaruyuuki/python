n = input()
m = int(input())
first = (m // len(n)) - 1
second = m - (first + 1) * len(n) - 1
if(second < 0 ):
    print(n[first] +n[second])
else:
    print(n[first+1] + n[second])