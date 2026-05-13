string = input()
array = string.replace('\\n',' ').split()
result = []
for l,r in zip(array,array[1:]):
    if not l[-1].isalpha() or not r[0].isalpha():
        continue
    if not l[0].isalpha(): 
        hold=[]
        seen=False
        for i in l:
            if i.isalpha():
                seen=True
            if seen:
                hold.append(i)
        l_clean=''.join(hold)
    else:
        l_clean=l
    if not r[-1].isalpha():
        idx=-1
        for i in range(len(r)-1,-1,-1):
            if r[i].isalpha():
                idx=i
                break
        r_clean=r[:idx+1]
    else:
        r_clean=r
    if l_clean.lower()==r_clean.lower():
        result.append(l_clean)
if result:
    for i in result:
        print(i)
else: print('No repeats!')
