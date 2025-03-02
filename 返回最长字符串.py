def main(lst):
    max=0
    maxstr=lst[0]
    for i in range(1,len(lst)):
        if len(lst[i])>max:
            max=len(lst[i])
            maxstr=lst[i]
    return maxstr
lst=input().split(",")
print(main(lst))