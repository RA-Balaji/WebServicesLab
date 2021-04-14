def calc(curr, volt):

    w = (curr[0] * volt[0])/(curr[1] * volt[1])
    
    return ([w/1000], [w], [w*1000])

def calc2(power, volt):
    
    w = (power[0] / volt[0]) * (power[1]  * volt[1])
    
    return (w, w * 1000)


print(calc2([10, 0.001], [2, 1000]))
#print(calc([2, 0.001], [4, 1000]))