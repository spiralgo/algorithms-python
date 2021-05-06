import math

def integral(f, a, b, dx = 0.0001):
    integral = 0
    while a <= b:
        integral += f(a)*dx
        a += dx
    return integral

def inf_sum(f, start = 1, end = 1000):
    sum = 0
    for k in range(start,end):
        sum += f(k)
    return sum

print(inf_sum(lambda x : ((-1)**(x+1)) * (1/x**2)))
print(inf_sum(lambda x: 1/x**6))

gaussian_integral = integral(lambda x: math.e**(-1*x*x), -1000,1000)
print(gaussian_integral)
print(gaussian_integral**2)