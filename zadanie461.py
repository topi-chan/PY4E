hrs = input("Enter Hours:")
pr = input("Enter rate:")
def computepay(h, p):
    if h <= 40.0:
        j = (p * h)
    else:
        j = (40 * p) + ((h - 40) * (p * 1.5))
    return print("Pay", j)
h = float(hrs)
p = float(pr)
computepay(h, p)
