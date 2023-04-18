import cmath

a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

# Вычисляем дискриминант
d = (b ** 2) - (4 * a * c)

# Находим корни уравнения
sol1 = (-b - cmath.sqrt(d)) / (2 * a)
sol2 = (-b + cmath.sqrt(d)) / (2 * a)

print("Корни квадратного уравнения", a, "x^2 +", b, "x +", c, "равны:")
print("x1 =", sol1)
print("x2 =", sol2)
