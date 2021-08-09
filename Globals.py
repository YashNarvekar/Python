a=10
b=20
c=30
d=40

def operations():
    global c,d
    c=c+1
    d=d+1
    print("Val of c(global var in function)=",c)
    print("val od d(global var in function)=",d)
    a=100
    b=200
    gva=globals()['a']
    gvb=globals()['b']
    print("Val of a(local var in function)=",a)
    print("Val of b(local var in function)=",b)
    print("Val of a(global var in function)=",gva)
    print("Val of a(global var in function)=",gvb)
    res=a+b+c+d+gva+gvb
    print("sum of all variable are:",res)


#main program
operations()