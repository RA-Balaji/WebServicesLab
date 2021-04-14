
def calc_log(x):

    num = x
    res = 0
    for i in range(0, 5):
        length = len(str(num))
        res = res + (length -1) * (10 ** (-i))
        #print(res)
        num = int((num/(10 ** (length -1))) ** 10)
        #print(num)
    
    return res

def ln(x):
    n = 1000.0
    return n * ((x ** (1/n)) - 1)

def anti_lg(x, y):
    return( x ** y)




#print(calc_log(25))
#print(ln(50))
print(anti_lg(10, calc_log(25)))