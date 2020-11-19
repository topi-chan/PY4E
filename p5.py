hrs = input("Enter Hours:")
h = float(hrs)
pr = input("Enter rate:")
p = float(pr)
if h <= 40:
    i = (p * h)
else:
    i = (40 * 10.5) + ((h - 40) * (p * 1.5))
print'Pay: ', i
