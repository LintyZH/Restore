def main(lst):
   clst=[]
   for item in lst:
      if item not in clst:
         clst.append(item)
   return clst
lst=input().split(",")
newlst=[int(i) for i in main(lst)]#将列表中的字符转换为数字
print(newlst)
