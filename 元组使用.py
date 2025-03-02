def main(p,q):
    t=(p//q,p%q)  #元组创建，元素值不能修改
    return t
a=int(input())
b=int(input())
print(main(a,b))