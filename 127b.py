inputnum = input().split(" ")
x = int(inputnum[0])
y = int(inputnum[1])
z = int(inputnum[2])
now = 0
for i in range(10):
    now = (x * z) - y
    print(now)
    z = now