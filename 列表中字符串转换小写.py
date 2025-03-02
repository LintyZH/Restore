def main(lst):
   lst=[i.lower() for i in lst]
   return lst
lst=input().split(",")
print(main(lst))
