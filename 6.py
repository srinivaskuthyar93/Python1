def calc(n1,n2):
    
    num1=n1
    num2=n2

    sum1=num1+num2
    sub1=num1-num2
    mult1=num1*num2
    div1=num1/num2
    div2=num1//num2
    rem1=num1%num2
    exp1=num1**num2
    print(sum1,sub1,mult1,div1,div2,rem1,exp1)
    
f1=open("in2.txt","r")
f2=open("out1.txt","w")
s1=f1.readline()
list1=s1.split(",")
n1=int(list1[0])
n2=int(list1[1])
calc(n1,n2)

f2.write("Srinivas")
f2.close()
