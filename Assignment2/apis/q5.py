def std_deviation(ele_li):

    x_mean = 0
    for i in ele_li:
        x_mean = x_mean + i
    x_mean = x_mean/len(ele_li)
    #print(x_mean)

    numerator = 0
    for i in ele_li:
        numerator = numerator + (((i - x_mean) ** 2))
    #print(numerator)
    res = (numerator/len(ele_li)) ** (1/2)

    return res

def variation(ele_li):
    return (std_deviation(ele_li) ** 2)

def linear_reg(x, y):

    x_sum = 0
    y_sum = 0
    xsq_sum = 0
    xy_sum = 0
    for i in range(0, len(x)):
        x_sum = x_sum + x[i]
        y_sum = y_sum + y[i]
        xsq_sum = xsq_sum + (x[i] ** 2)
        xy_sum = xy_sum + (x[i] * y[i])
    print(x_sum)
    print(y_sum)
    print(xy_sum)
    print(xsq_sum)
    
    b = ((len(x) * xy_sum) - (x_sum * y_sum))/((len(x) * xsq_sum) - (x_sum ** 2))

    a = (y_sum - (b * x_sum))/len(x)

    return "Y = " + str(a) + "X " + "+ " + str(b)
    

#print(std_deviation([4, 9, 11, 12, 17, 5, 8, 12, 14]))
#print(variation([4, 9, 11, 12, 17, 5, 8, 12, 14]))
print(linear_reg([2,3,5,8], [3,6,5,12]))