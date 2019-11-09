n=int(input())
jobs = {}

for i in range(n):
    needTime, deadLine = map(int,input().split(' '))
    if(deadLine in jobs):
        jobs[deadLine] += needTime
        continue
    jobs[deadLine] = needTime
sortJobs = sorted(jobs.items(), key=lambda x:x[0])

nowDay = 0
for deadLine,needTime in sortJobs:
    nowDay+=needTime
    if(nowDay>deadLine):
        print('No')
        exit()
else:
    print('Yes')