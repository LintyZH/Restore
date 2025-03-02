def main(lst):
   for i in range(0,len(lst)):  #0----n-1
     for j in range(0,len(lst)-i):#j=i--n-1
        if(len(lst[j])>len(lst[j+1])):
           lst[j+1],lst[j]=lst[j],lst[j+1]
   return lst
lst=input().split(",")
print(main(lst))
