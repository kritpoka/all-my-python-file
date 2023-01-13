import numpy as np

def dot_product():
    v1,v2,v3 = [int(e) for e in input().split()]
    u1,u2,u3 = [int(e) for e in input().split()]

    v = np.array([v1,v2,v3])
    u = np.array([u1,u2,u3])

    dot = v.dot(u)

    print(dot)

def dot_product2():
    a = [1,3,-5]
    b = [4,-2,-1]

    np.dot(a,b)

    a=np.array([3,-5,+6])
    b=np.array([0,2,0])

    a.dot(b)

    print(a)
    print(b)



