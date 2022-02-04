f1 = open("file1.txt","r")
f2 = open("file2.txt","r")

x=''

while(x in f1):
    print(x)
    for y in f2:
        if x == y:
            print("dup")
        else:
            print("No")

"""
for x in f1:
    f1_val=x
    print(x)
    for y in f2:
        f2_val=y
        if f2_val == f1_val:
            print(x,y+"Duplicate")
        else:
            print(x,y+"Not ")

"""

"""
for i in f1:
    vf1=f1.readline()
    for j in f2:
        if vf1== f2.readline():
            print(vf1+"duplicate")
        else:
            print("Not duplicate")

"""




