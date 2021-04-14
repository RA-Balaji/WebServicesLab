def factorial(n):

    fact = 1
    for i in range(2, n+1):
        fact = fact * i
    
    return fact

def calc_sin(x):
    rad = (x/180) * (22/7)
    #print(rad)

    sin = 0
    for i in range(0, 11):
        sin = sin + ((((-1) ** i)/factorial(2*i + 1)) * (rad ** (2*i +1)))
    return sin

def calc_cos(x):
    rad = (x/180) * (22/7)
    #print(rad)

    cos = 0
    for i in range(0, 11):
        cos = cos + (((-1) ** i)/factorial(2*i)) * (rad ** (2*i))
    return cos

def calc_tan(x):
    if x == 90 or x == 270:
        return "undefined"
    else:
        return (calc_sin(x)/calc_cos(x))

def secx(deg):
    if(( deg == 90) or (deg == 270)):
        return 'undefined'
    return 1/calc_cos(deg)


def cosecx(deg):
    if(( deg == 0) or (deg == 180)):
        return 'undefined'
    print(1/calc_sin(deg))
    return (1/calc_sin(deg))


def cotx(deg):
    if(( deg == 0) or (deg == 180)):
        return 'undefined'
    return calc_cos(deg)/calc_sin(deg)


def calc_arctan(x):
    arctan = 0
    for i in range(0, 50): 
        arctan += ((-1) ** i) * ((x**(2 * i + 1)) / (2 * i + 1))
    return arctan*57.2958

def calc_arccos(x):
    temp = ((1- (x**2)) ** 0.5)/x
    return calc_arctan(temp)
    
def calc_arcsin(x):
    temp = x/((1- (x**2)) ** 0.5)
    return calc_arctan(temp)

#print(factorial(6))
#print(calc_sin(90))
#print(calc_cos(0))
#print(calc_arctan(45))
print(cosecx(30))