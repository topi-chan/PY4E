hrs = input("Enter Hours:")
rte = input("Enter Rate:")
h = float(hrs)
p = float(rte)
def computepay():
    if h <= 40:
        j = (p * h)
        print('Pay:', j)
    else:
        j = (40 * 10.5) + ((h - 40) * (p * 1.5))
        print('Pay:', j)
computepay()
