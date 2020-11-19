def computepay(h,p):
    if h <= 40:
        j = (p * h)
        print(j)
    else:
        j = (40 * 10.5) + ((h - 40) * (p * 1.5))
        print(j)
computepay(10,10.5)
