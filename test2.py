temperature = [1, -2, -8, 4, 5]

if not temperature:
    print(0)

else:
    closest = temperature[0]
    for t in temperature:
        if abs(t) < abs(closest):
            closest = t

print(closest)
