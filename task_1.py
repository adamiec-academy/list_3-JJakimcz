def is_perfect(n):
    helper=[]
    for i in range(1,n):
        if (n % i) == 0 and n!=i:
            helper.append(i) 

    if sum(helper) == n:
        return True


def get_perfect_numbers(n):
    i=0
    ln=[]
    while len(ln) != n:
        i+=1
        if (is_perfect(i)) == True:
            ln.append(i)
            
    for u in range(len(ln)):
        print (ln[u] ," ",end="")

get_perfect_numbers(n)
