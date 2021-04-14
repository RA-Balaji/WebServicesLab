import random

def toIntList(inp, delim):
    return list(map(int, inp.split(delim)))


def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a


def modulo_multiplicative_inverse(e,phi):
    
    gcd, x, y = extended_euclid_gcd(e, phi)

    print(gcd,x,y)

    if x < 0:
        x += phi
    
    return x


def extended_euclid_gcd(a, b):
 
    s = 0; prev_s = 1
    t = 1; prev_t = 0
    r = b; prev_r = a

    while r != 0:
        quotient = prev_r//r 

        prev_r, r = r, prev_r - quotient*r
        prev_s, s = s, prev_s - quotient*s
        prev_t, t = t, prev_t - quotient*t
    
    return [prev_r, prev_s, prev_t]



def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True


def generate_keypair(p, q):
        if not (is_prime(p) and is_prime(q)):
            raise ValueError('Both numbers must be prime.')
        elif p == q:
            raise ValueError('p and q cannot be equal')
        n = p * q
        phi = (p-1) * (q-1)
        e = random.randrange(1, phi)
        g = gcd(e, phi)


        # checking whether e is co-prime iteratively
        while g != 1:
            e = random.randrange(1, phi)
            g = gcd(e, phi)
        print("e   :",e," \nphi :", phi )    
        
        d = modulo_multiplicative_inverse(e, phi)
        print(d,e)
        return ((e, n), (d, n))