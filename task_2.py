def fibonacci_sequence(n):
    

    if n==0:
        l1=[]
        return l1
    if n==1:
        l2=[0]
        return l2

    fibonacci = [0, 1]
    for i in range(2,n):
        
        fibonacci.append(fibonacci[i-1]+fibonacci[i-2])

    print (fibonacci)
    return fibonacci
