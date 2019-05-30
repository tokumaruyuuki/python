inputString = input()

ans = inputString.lower()
strlist = list(ans)
tmp =  ans[0].upper()
ansarray = tmp + "".join(ans[1:])
print(ansarray)