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

n1=int(input("Enter first number"))
n2=int(input("Enter second number"))
calc(n1,n2)

