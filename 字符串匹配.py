def main(lst,item):
    c=lst.count(item)
    if c > 0:
        print(lst.index(item))
    else:
        print("'不存在'")
lst=input().split()
item=input()
main(lst,item)