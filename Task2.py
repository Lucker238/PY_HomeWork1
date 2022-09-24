# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
x, y, z = int(input('Введите х: ')), int(input('Введите y: ')), int(input('Введите z: '))
left = not(x or y or z)
right = not x and not y and not z
check = left == right
print(check)