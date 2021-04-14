
def gcd(a,b):
     
    if (a == 0):
        return b
    if (b == 0):
        return a

    if (a == b):
        return a

    if (a > b):
        return gcd(a-b, b)
    return gcd(a, b-a)
 
def lcm(a,b):

    if a>b:
        max_num = a
    else:
        max_num = b
    
    while(True):
        if( max_num % a== 0 and max_num % b == 0):
            lcm = max_num
            break
        max_num = max_num + 1
    return lcm


def sq_rt(a):
    return a ** (1/2)

def cube_rt(a):
    return a ** (1/3)

def n_rt(a, n):
    return a ** (1/n)

#print(n_rt(27, 3))
#print(cube_rt(27))
#print(sq_rt(16))