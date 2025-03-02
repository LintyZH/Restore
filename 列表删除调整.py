def main(lst):
    result=0
    for i in range(0,len(lst)):
        result+=int(lst[i])
    result/=len(lst)
    newlst=[]
    for i in range(0,len(lst)):
        if int(lst[i])>=result:
            newlst.append(lst[i])
    return newlst
lst=input().split()
lst=main(lst)
print(lst)