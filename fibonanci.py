#1, 1, 2, 3, 5, 8
def fibonanci(loop):
    temp=[]
    a=0
    temp.append(1)
    for i in range(0,loop-1):
        if(a==0):
            a+=1
            temp.append(a)   
        else:
            val=temp[i-1]+temp[i]
            temp.append(val)
    return temp
print(fibonanci(18))