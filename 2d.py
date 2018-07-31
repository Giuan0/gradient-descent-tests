import matplotlib.pyplot as plt


def function(x):
    return x**2
def derivate_of_function(x):
    return 2*x

lr = 0.1

axes = list(range(-10, 11))
fx   = [function(x) for x in axes ]

x_history = []
x = -9 #initial value
n = 10
for i in range(n):
    print(x)
    x_history.append(x)
    #x = x - ( f'(x) * -1)
    x += (derivate_of_function(x) *-1) * lr


fx_history = [function(g) for g in x_history]

plt.plot(axes, fx)
plt.plot(x_history, fx_history , 'co')
plt.show()