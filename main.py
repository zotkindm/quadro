# ax2 + bx + c = 0
#
# Вычисляется дискриминант уравнения по формуле:  D = b**2-4ac
#   D > 0 - два корня
#   D = 0 - один корень
#   D < 0 - корней нет
#
# Корни x1 и x2
#   x1 = (0-b + sqd(D))/2a
#   x2 = (0-b - sqd(D))/2a
a, b, c = 1,2,-200

def Discriminant(a, b, c):
    D = b**2 - 4 * a * c
    return float(D)

class X:
    def X1(self):
        return (-b - Discriminant(a, b, c) ** 0.5) / 2 * a
    def X2(self):
        return (-b + Discriminant(a, b, c) ** 0.5) / 2 * a
x = X()

print('\n', 'D =', Discriminant(a, b, c),'\n')

if Discriminant(a, b, c) == 0:
    print('Один корень', x.X1())

elif Discriminant(a, b, c) < 0:
    print('Корней нет')

else:
    print('два корня:\n', 'x1 =',x.X1(),'\n','x2 =',x.X2())
