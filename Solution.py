def clean(s) -> str:
    if not s[0].isalpha():
        for i in range(len(s)):
            if s[i].isalpha():
                return s[i:]
    else:
        for i in range(len(s)-1,-1,-1):
            if s[i].isalpha():
                return s[:i+1]
    return ""

array = input().replace('\\n',' ').split()

index = 0
words = 0

while index<len(array)-1:
    if array[index][-1].isalpha():
        test = clean(array[index]).lower()
    else:
        index+=1
        continue
    count=0
    for i in range(index+1,len(array)):
        if not array[i][0].isalpha():
            break

        if array[i].lower()!=test:
            if clean(array[i]).lower()==test:
                count+=1
            break
        count+=1
    if count>0:
        print(clean(array[index]))
        words+=1
        index+=count
    index+=1
if words==0:
    print('No repeats!')
