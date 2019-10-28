people, legs = map(int,input().split(' '))
two, tree , four = 2,3,4

#老人が０の場合
falg = False
for i in range(people+1):
    if ((i*two + (people - i)*four) == legs):
        print(i,0,people - i)
        falg = True
        break
for i in range(people):
    if(i*two + (people-i-1)*four + 3 == legs):
        print(i,1,people-i-1)
        falg = True
        break
if (not falg):
    print(-1,-1,-1)
#老人が１の場合