import math
def discriminant(a, b, c):
    """
    функция для нахождения дискриминанта
    """
    return b ** 2 - 4 * a * c

def solution(a, b, c):
    """
    функция для нахождения корней уравнения
    """
    d = discriminant(a, b, c)
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print(x1, x2)
    elif d == 0:
        x3 = -b/(2*a)
        print(x3)
    else:
        print('корней нет')
if __name__ == '__main__':
    solution(1, 8, 15) 
    solution(1, -13, 12)
    solution(-4, 28, -49)
    solution(1, 1, 1)
