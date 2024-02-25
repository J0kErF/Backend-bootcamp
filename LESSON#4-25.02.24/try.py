def dup(lst,index=0):
    if 2*index==len(lst):
        return lst
    lst.append(lst[index])
    return dup(lst,index+1)
def dup1(lst):
    return lst+lst
def dup2(lst):
    return lst*2
def dup3(lst):
    new_lst=lst[1:]
    length=len(new_lst)
    return [lst[0]]+dup3(new_lst)+[lst[length]] if lst else []
def dup4(lst):
    for i in range(len(lst)):
        if lst[i] is list:
            lst.append(lst[i])
        lst.append(lst[i])
print(dup3([1,2,[3],4]))