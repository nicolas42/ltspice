import math
import cmath


def transfer_function(s,r,c):
    r1 = r
    r2 = r
    c1 = c 
    c2 = c

    return 1/( r1*r2*c1*c2*s*s + (r1+r2)*c2*s + 1 )

# s = j*w
# w = 2*pi*f
# s = j*2*pi*f

f = 150
s = complex(0, 2*math.pi*f)
c = 0.1e-6
r = 11e3


print(transfer_function(s,0.98*r,c))
print(transfer_function(s,r,c))
print(transfer_function(s,r,c))
print(transfer_function(s,r,c))


print(result)

