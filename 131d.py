n = int(input())
 
task = {}
for i in range(n):
    tmp = list(map(int , input().split(" ")))
    if(tmp[1] in task):
        task[tmp[1]].append(tmp[0])
    else:
        task[tmp[1]] = [tmp[0]]
 
time = 0
time_sorted = sorted(task.items(), key=lambda x:x[0])
flag = 0
#print(time_sorted)
for limit,need in time_sorted:
    time += sum(need)
    if(time > limit):
        flag += 1
        break;
 
if(flag == 1):
    print("No")
else:
    print("Yes")