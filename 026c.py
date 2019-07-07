n = int(input())

staff = [0] * (n)
nostaff = [0] * n
for i in range(1,n):
    staffId = int(input())
    staff[i] = staffId-1
    nostaff[staffId-1] += 1

salary = [0] * n
for i in reversed(range(n)):
    if(nostaff[i] == 0):
        salary[i] = 1
    else:
        tmpArray = []
        for staffid in range(1,n):
            if(staff[staffid] == i):
                tmpArray.append(salary[staffid])
        salary[i] = max(tmpArray) + min(tmpArray) + 1
print(salary[0])
