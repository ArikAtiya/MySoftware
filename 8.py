seven_boom = list(range(0, 100))
for i in seven_boom:
    if not (i % 7 == 0 or '7' in str(i)):
        print(i)