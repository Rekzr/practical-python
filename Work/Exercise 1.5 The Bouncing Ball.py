height = 100
bounceMult = 3 / 5
bounce = 1
while bounce <= 10:
    height *= bounceMult
    bounce += 1
    print(round(height, 4))
