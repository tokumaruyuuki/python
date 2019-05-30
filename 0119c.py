x = input().split()

bumbues = int(x[0])
a = int(x[1])
b = int(x[2])
c = int(x[3])

ans = 0
bumbues_list = []

for i in range(bumbues):
    y = input()
    bumbues_list.append(int(y))

def just_long(want_long,left_bumbues):
    for i in range(left_bumbues):
        if bumbues_list[i] == want_long:
            del bumbues_list[i]
            return True
    return False

def most_near_long(want_long,left_bumbues,first_or_second):
    global ans
    '''
    このメソッドでは、目的の長さと残りの竹の数を受け取る。
    具体的な目的としては、配列内で一番もくてきちに近いものを探すことだが、少し注意点がある上に、分岐点を与えて少し処理を加える必要がある。
    しかも、まだこのメソッドを使って組み合わせ要素を探すなら数字を、違うならfalseを返す。
    まず、行うのは
    １：今の長さと残りの要素の長さを組み合わせて一番近くになる組み合わせを調べる。
    ことだが、ここで、
    ＊：１０以内の長さ変更なら、単純に延長・縮小を加えていくほうがよい。false
    ということ。
    次に、
    ２：もし、その最適な組み合わせが（目標の長さー今の長さ）＜＝（１０＋組み合わせ後の長さの不足分）となるならば、組み合わせるべきではない。false
    ということも、コードに組み込むべき。
    
    殴り書きみたいになったが、このような意図でメソッドを書いていく。
    順番としては
    ・まず、要素内で一番条件に近い数を調べる。
    ・その数が１０以下ならもう調べる必要はない。
    ・次に、（目標の長さー今の長さ）＜＝（１０＋組み合わせ後の長さの不足分）の判断。これも当てはまるようなら中断。
    ・これらの条件をクリアしたら、その次のループも回すべきだと判断。
    ・そして、答えに＋１０をしておく。そしてその要素を消しておく。
    ・そして、次にループを回すなら数字を。ループしないならfalseを返してループを止める。
    '''
    if want_long <= 10:
        ans += want_long
        return False
    
    diff = 10000
    diff_index = 0
    for i in range(left_bumbues):
        length2 = want_long - bumbues_list[i]
        if length2 < 0:
            length2 *= -1
            
        if length2 <= diff:
            diff =  length2
            diff_index = i
    if diff <= 10:
        ans += diff
        del bumbues_list[diff_index]
        return False
    elif first_or_second == 1:
        if want_long <= (10 + diff):
            return False
    del bumbues_list[diff_index]
    ans += 10
    return diff
    
    
    
#ここからメイン部分


for i in range(3):
    now_serch = 0
    if i == 0:
        now_serch = a
    elif i == 1:
        now_serch = b
    elif i == 2:
        now_serch = c
    
    if just_long(now_serch,len(bumbues_list)): #just_longはちょうど求めるものと同じ長さのものがあった場合に、その要素を消して戻り値はtrueを返すメソッド
        continue
    else:
        length = most_near_long(now_serch,len(bumbues_list),0)
        while length: #most_near_longは最も目的の数字に近づけるメソッド。でも、中身の実装はメソッド内の注意に。
            length = most_near_long(length,len(bumbues_list),1)



print(ans)
    

#できない
ーーーーーーーーーーーーーーーー

N,A,B,C = map(int ,input().split(" "))
a_b_c = [A,B,C]
bamboo = list()
ans = 0
for i in range(N):
    y = input()
    bamboo.append(int(y))

bamboo.sorted().reverse()

def find_length(abc):
    global ans
    difference = float("inf")
    index = 0
    for i in range(bamboo):
        length = bamboo[i] - abc
        if length < 0:
            length *= -1
        if length < difference:
            index = i
            difference = length
    if difference == float("inf"):
        return True
    elif difference <= 10:
        bamboo.pop(index)
        ans += difference + 10
        return True
    elif abc + difference  <= 10:
        ans += abc
        return True
    else:
        abc -= bamboo[index]
        bamboo.pop(index)
        ans += 10
        find_length(abc)

for abc in a_b_c:
    
    
    