def fac(n) :
    if n == 1 :
        return 1
    return n * fac(n-1)
    
#Bài 1
print("Bài 1")
first = 1
x = 0.5
eps = 0.000001
mu =1
second = first + x**mu / mu
count = 0
print("x =", second)
while abs(first - second) > eps:
    mu -= -1
    first = second
    second = first + x**mu / mu
    count+=1
print("KQ: ", second)

#Bài 2
print("Bài 2")
first = 1
x = 0.5
temp = 1
dau = -1
eps = 0.000001
second = first + dau*(((temp + 1)*(temp + 2))/2)*x*temp
print("x =", second)
while abs(first - second) > eps:
    temp -= -1
    dau = -dau
    first = second
    second = first + dau*(((temp + 1)*(temp + 2))/2)*x*temp
print("KQ: ", second)

#Bài 3
print("Bài 3")
first = 0.5
x = 0.5
temp = 2
eps = 0.000001
second = -1*first - (x*temp/temp)
print("x =", second)
while abs(first - second) > eps:
    temp -= -1
    first = second
    second = first - (x*temp/temp)
print("KQ:", second)

#Bài 4
print("Bài 4")
first = 1
x = 0.5
mu = 1
dau = -1
eps = 0.000001
n = 0
temp = (0.5) * x**mu
second = first + (0.5) * x**mu
print("x =", second)
while abs(first - second) > eps:
    tu = 1
    mau = 4
    mu -= 1
    n = mu
    temp = (0.5) * x**mu
    first = second
    while(n>1):
        temp = temp * (tu/mau)
        tu = tu + 2
        mau = mau + 2
        n-=1
    second = first + dau * temp
    dau = -dau
print("KQ:", second)

#Bài 5
print("Bài 5")
first = 1
x = 0.5
mu = 1
dau = -1
eps = 0.000001
n = 0
temp = 0
second = first - (0.5)*x ** mu
print("x =", second)
while abs(first - second) > eps:
    tu = 3
    mau = 4
    mu-=-1
    n=mu
    temp= (0.5)*x ** mu
    first = second
    while n>1:
        temp =temp*(tu/mau)
        tu= tu+2
        mau=mau+2
        n -= 1
        dau = - dau
    second = first + dau*temp
print("KQ: ",second)

#Bài 6
print("Bài 6")
x = 0.5
eps = 0.00001
mu = 3
dau = -1
first = 0.5
second = first - x**mu / fac(mu)
print ("x = ", second)
while abs(first - second) > eps:
    mu+=2
    first = second
    second = first - (dau * x**mu / fac(mu))
    dau = -dau
print ("KQ: ", second)

#Bài 7
print("Bài 7")
x = 0.5
eps = 0.000001
mu = 2
dau = -1
first = 1
second = first - x**mu / fac(mu)
print ("x = ", second)
while abs(first - second) > eps:
    mu+=2
    first = second
    second = first - (dau * x**mu / fac(mu))
    dau = -dau
print("KQ: ", second)

#Bài 8
print("Bài 8")
x = 0.5
eps = 0.000000001
mu = 3
tu = 3
mau = 4
first = 0.5
count =0
n = 0
temp = 0
second = first + 0.5*x ** mu/mu
print("x =",second)
while abs(first - second) > eps:
    mu+=2
    count += 1
    n=count
    temp= (0.5)*x ** mu/mu
    first = second
    while n>0:
        temp =temp*(tu/mau)
        tu= tu+2
        mau=mau+2
        n -= 1
    second = first + temp
print("KQ: ", second)

#Bài 9
print("Bài 9")
x = 0.5
eps = 0.000001
mu = 1
dau = -1
first = 1
second = first - x**(mu + 1) / fac(mu + 2)
print("x = ", second)
while abs(first - second) > eps:
    mu+=2
    first = second
    second = first - (dau * x**(mu + 1) / fac(mu + 2))
    dau = -dau
print("KQ: ", second)

#Bài 10
print("Bài 10")
x = 0.5
eps = 0.000000001
mu = 3
dau =-1
first = x
second = first - x ** mu / mu
print("x = ", second)
while abs(first - second) > eps:
    mu+=2
    first = second
    second = first - (dau * x ** mu / mu)
    dau = - dau
print("KQ: ",second)

#Bài 11
print("Bài 11")
x = 0.5
eps = 0.000000001
mu = 2
dau =-1
first = 0.5
second = first - x ** mu / mu
print("x = ", second)
while abs(first - second) > eps:
    mu-=-1
    first = second
    second = first - (dau * x ** mu / mu)
    dau = - dau
print("KQ: ", second)

#Bài 12
print("Bài 12")
x = 0.5
eps = 0.000000001
mu = 3
first = x
second = first + x ** mu / mu
print("x = ", second)
while abs(first - second) > eps:
    mu+=2
    first = second
    second = first +x ** mu / mu
print("KQ: ",2*second)

#Bài 13
print("Bài 13")
x = 0.5
eps = 0.000000001
mu = 3
first = 0.5
second = first + x**mu / fac(mu)
print("x =", second)
while abs(first - second) > eps :
    mu += 2
    first = second
    second = first + x**mu / fac(mu)
print("KQ: ", second)

#Bài 14
print("Bài 14")
x = 0.5
eps = 0.000000001
mu = 2
first = 1
second = first + x ** mu / fac(mu)
print("x =", second)
while abs(first - second) > eps:
    mu+=2
    first = second
    second = first +x ** mu / fac(mu)
print("KQ: ",second)
