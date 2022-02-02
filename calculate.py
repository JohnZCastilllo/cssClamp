# visit this link for more
# https://www.aleksandrhovhannisyan.com/blog/fluid-type-scale-with-css-clamp/

def calculate(maxF,minF,maxB,minB):
    
    # m for the viewport width
    # b for the constant added to m
    
    m = (maxF - minF) / (maxB - minB)
    b = minF - (m * minB)
    
    #checking if correct result
    print('Correct for min: ',m*minB+b == minF)
    print('Correct for max: ',m*maxB+b == maxF)
    
    # * 100 to convert to vw (according to the link above)
    m = round(m*100)

    # print integer value
    print("clamp(%dpx, %svw + %dpx, %dpx)" % (minF,m,b,maxF))
    
#max font, min font, max Breakpoint, minimum breakpoint
calculate(38,17,1440,375)

