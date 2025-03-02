
from operator import mul
def main(vector1,vector2):
    vector1=[int(i) for i in vector1]
    vector2=[int(i) for i in vector2]
    list=map(mul,vector1,vector2)
    return sum(list)  
v1=input().split(",")
v2=input().split(",")
print(main(v1,v2))
