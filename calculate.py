def calculate(maxF,minF,maxB,minB):
    m = (maxF - minF) / (maxB - minB)
    b = minF - (m * minB)
    print(m*maxB + b)
    print(round(m*100,2),round(b,2))

#max font, min font, max Breakpoint, minimum breakpoint
#calculate(19,16,1000,400)
calculate(47,19,1440,375)
