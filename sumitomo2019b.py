n = int(input())
ans= n // (1.08)
ans1 = ans +1
ans2 = ans -1
 
if(int(ans1 * (1.08)) == n):
    print(int(ans1))
elif(int(ans2 * (1.08)) == n):
    print(int(ans2))
elif(int(ans * (1.08)) == n):
    print(int(ans))
else:
    print(':(')