def trapezoid_area(height, base1, base2):
    area = 0.5 * (base1 + base2) * height
    return area

height = 5
base1 = 5
base2 = 6
area = trapezoid_area(height, base1, base2)
print("Height:", height)
print("Base, first value:", base1)
print("Base, second value:", base2)
print("Expected Output:", area)
