def fibonacci_sequence(n):
    fibonacci=[]
    x=0

    while len(fibonacci) != n:
        if (x<3):
            if (x==0):
                fibonacci.append(0)
                x+=1
                continue
            elif (x==1) or (x==2):
                fibonacci.append(1)
                x+=1
                continue       
        a = fibonacci[x-1]+fibonacci[x-2]
        fibonacci.append(a)
        x+=1
        return fibonacci

fibonacci_sequence(n)
