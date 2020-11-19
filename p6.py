try:
    hrs = input("Enter Hours:")
except:
    print('Error, please enter numeric input!')
    quit()
try:
    pr = input("Enter Rate:")
except:
    print('Error, please enter numeric input!')
    quit()
h = float(hrs)
p = float(pr)
if h <= 40:
    i = (p * h)
else:
    i = (40 * 10.5) + ((h - 40) * (p * 1.5))
print'Pay: ', i
