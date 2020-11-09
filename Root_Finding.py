import math
X= input("Hangi şıkkın cevabını istiyorsunuz?")
if X=="a":
    def f(x):
        return (math.e**x)-3*x**2
    def df(x):
        return (math.e**x)-6*x

elif X=="b":
    def f(x):
        return x**3-x**2-x-1
    def df(x):
        return 3*x**2-2*x-1
elif X=="c":
    def f(x):
        return (math.e**x)-1/(0.1+x**2)
    def df(x):
        return (math.e**x)+2*x/(x**2+0.1)**2
elif X=="d":
    def f(x):
        return x-1-0.3*math.cos(x)
    def df(x):
        return (3*math.sin(x)/10)+1
#Bisection Method
xp = 100
xn = -100
y=100
iter_a=0
if f(xp)<0:
    xp = -100
    xn = 100
while abs(y)>10**(-5):
    x_a=(xp+xn)/2
    iter_a=iter_a+1
    if f(x_a)<0:
        xn=x_a
    else :
        xp=x_a
    y = f(x_a)
print("x ",x_a)
print("y ",y)
print("Bisection Methodu ile ",iter_a," iterasyonda bulundu.")
#Newton Raphson Methodu
x_b=0
iter_b=0
while abs(f(x_b))>10**(-5):
    iter_b=iter_b+1
    if df(x_b)==0:
        print("Türev=0 Newton Raphson İle çözüm bulunamadı")
    x_b=x_b-f(x_b)/df(x_b)
print("x ",x_b)
print("y ",f(x_b))
print("Newton Raphson Methodu ile çözüm ",iter_b," iterasyonda bulundu.")
#Secant Metodu
x_c_0=-10
x_c_1=10
x_c_2=0
iter_c=0
while abs(f(x_c_1))>10**(-5):
    iter_c=iter_c+1
    x_c_2=x_c_1-f(x_c_1)*(x_c_1-x_c_0)/((f(x_c_1)-f(x_c_0)))
    x_c_0=x_c_1
    x_c_1=x_c_2
print("x ",x_c_1)
print("y ",f(x_c_1))
print("Secant Methodu ile çözüm ",iter_c," iterasyonda bulundu.")