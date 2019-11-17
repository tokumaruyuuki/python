member = int(input())
time_table = []
for i in range(5):
    time_table.append(int(input()))
send_member_pre_second = min(time_table)
time1 = member // send_member_pre_second
ans = time1+5
if(time1 > send_member_pre_second and time1%send_member_pre_second==0):
    ans-=1
print(ans)